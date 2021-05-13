mod=10**9+7
N,K=map(int,input().split())
ans=0
for i in range(K,N+2):
    MIN=(i*(i-1))//2
    MAX=((N+1)*N)//2-((N-i+1)*(N-i))//2
    ans+=MAX-MIN+1
    ans%=mod
    #print(i,MIN,MAX)
print(ans)