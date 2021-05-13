N,K = map(int,input().split())
pls = list(map(int,input().split()))
ans = sum(pls[:K])/2 + 0.5*K
sum1 = ans
for i in range(1,N-K+1):
    sum1 += -pls[i-1]/2+pls[i+K-1]/2
    ans = max(ans,sum1) 
print(ans)