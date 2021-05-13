N, X=map(int, input().split())
ans=[]
for _ in range(X-N+1, X+N):
  ans.append(str(_))
print(" ".join(ans))
