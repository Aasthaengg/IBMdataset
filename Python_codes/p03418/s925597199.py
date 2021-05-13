N,K = list(map(int,input().split()))
ans=0

for b in range(N):
    b+=1
    alpha = N//b
    beta = N % b
    
    ans += max(0,b-K)*alpha
    ans += max(0,beta-K+1)
    
    if K == 0:
        ans -= 1
    
print(ans)