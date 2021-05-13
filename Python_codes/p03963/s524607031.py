n,k=input().split()
N=int(n)-1
K=int(k)-1
ans=K+1
for i in range(N):
    ans*=K
print(ans)  