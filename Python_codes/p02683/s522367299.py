N,M,X=map(int,input().split())
CA=[list(map(int,input().split())) for _ in range(N)]
max_=10**16
ans=max_
for bit in range(2**N):
  check=[0]*M
  ans_=0
  for i in range(N):
    if bit>>i&1:
      ans_+=CA[i][0]
      for j in range(M):
        check[j]+=CA[i][j+1]
  if all([k>=X for k in check]):
    ans=min(ans,ans_)
print(ans if ans!=max_ else -1)
