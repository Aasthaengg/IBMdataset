def I(): return int(input())
n = I()
ans = 0
if n>=105:
    for i in range(105,n+1,2):
        cnt=0
        for j in range(1,int(i**0.5)+1):
            if i % j ==0:
                if j*j==i:
                    cnt+=1
                else:
                    cnt+=2
        if cnt==8:
            ans+=1
print(ans)
