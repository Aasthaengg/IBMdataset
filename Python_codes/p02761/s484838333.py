N,M=map(int,input().split())
if N==1:
  ans=["0"]
else:
  ans=["1"]+["0"]*(N-1)
check=[0]*N
for _ in range(M):
  s,c=map(int,input().split())
  if check[s-1]==0:
    check[s-1]=c
  elif check[s-1]!=c:
    print(-1)
    exit()
  ans[s-1]=str(c)
if len(ans)==1:
  print("".join(ans))
else:
  print("".join(ans) if ans[0]!="0" else -1)
