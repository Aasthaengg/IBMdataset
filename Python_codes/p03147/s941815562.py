#ABC 116 C - Grand Garden

n = int(input())
h = list(map(int, input().split()))

#リストの最大値Mを求める
#リストを左から走査
 #MだったらフラグOn、その数を-1。Mより下回ったらフラグoff
 #までいったらMを

cnt = 0
while max(h) > 0:
    M = max(h)
    for i in range(n):
        if i == 0:
            flag = False
        
        if h[i] == M and flag == False:
            cnt += 1
            h[i] -= 1
            flag = True
        
        elif h[i] == M and flag == True:
            h[i] -= 1
            
        else:
            flag = False
        
print(cnt)