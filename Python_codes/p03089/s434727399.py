n=int(input())
b=list(map(int,input().split()))
ans=[]
while n>=1:
  for i in range(len(b)-1,-1,-1):
    if i+1==b[i]:
      t=b.pop(i)
      ans.append(t)
      break
  if n == len(b):
    break
  n-=1
ans=reversed(ans)
if n==0:
  for i in ans:
    print(i)
else:
  print(-1)