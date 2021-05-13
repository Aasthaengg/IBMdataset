N,K=map(int, input().split())
P=list(map(int, input().split()))

Q=sorted(P)
ans=0
for i in range(K):
  ans+=Q[i]
print(ans)