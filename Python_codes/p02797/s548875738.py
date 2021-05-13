N,K,S=map(int,input().split())
ans=[]

if S<10**9:
    ans=[S for i in range(K)]
    ans+=[S+1 for i in range(N-K)]
else:
    ans=[S for i in range(K)]
    ans+=[1 for i in range(N-K)]

print(*ans)