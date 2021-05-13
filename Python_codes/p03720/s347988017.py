n,m = list(map(int, input().split()))
ans=[0]*n
for i in range(m):
  a,b=list(map(int, input().split()))
  a,b=a-1,b-1
  ans[a],ans[b]=ans[a]+1,ans[b]+1
for i in range(n):
  print(ans[i])
