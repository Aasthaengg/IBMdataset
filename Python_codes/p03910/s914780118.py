N = int(input())

def search_ans(max,min):
    if max - min <= 4:
        for i in range(min,max+1):
            if (1+i)*i/2 >= N: #n問目まで全てOKだったときの合計得点… (1+n)*n/2 
                return i
                
    else:
        mid = int((max+min)//2)

        if (1+mid)*mid/2 < N:
            min = mid
        else:
            max = mid
            
        return search_ans(max,min)
    
ans_max = search_ans(N,1) #最大値を探す

for i in range(ans_max,0,-1):
    if N - i >= 0:
        print(i)
        N -= i