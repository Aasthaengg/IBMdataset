n=int(input())
b=list(map(int,input().split()))
ans=[]
for i in range(n):
  if b[i]-1>len(ans):
    print(-1)
    break
  else:
    ans.insert(b[i]-1,b[i])
else:
  for i in range(n):
    print(ans[i])
