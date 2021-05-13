K,N=map(int,input().split())
A=[int(i) for i in input().split()]
B=A+[i+K for i in A]
ans=K
for i in range(N):
    tmp=B[i+N-1]-B[i]
    ans=min(ans,tmp)
print(ans)
