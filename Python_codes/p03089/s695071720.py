N=int(input())
b=list(map(int, input().split()))
ans=[]
for i in range(N):
  for j in range(len(b)-1, -1, -1):
    if b[j]==j+1:
      ans.append(b.pop(j))
      break
      
if len(ans)<N:
  print(-1)
else:
  for i in range(N-1, -1, -1):
    print(ans[i])
