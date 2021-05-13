n=int(input())
a=list(map(int,input().split()))
ans=[]
if max(a)>-min(a):
  x=max(a)
  idx=0
  for i in range(n):
    if a[i]==x:
      idx=i
      break
  for i in range(n):
    if a[i]==a[idx]:
      continue
    ans.append((idx+1,i+1))
  for i in range(n-1):
    ans.append((i+1,i+2))
else:
  x=min(a)
  idx=0
  for i in range(n):
    if a[i]==x:
      idx=i
      break
  for i in range(n):
    if a[i]==a[idx]:
      continue
    ans.append((idx+1,i+1))
  for i in range(n-1)[::-1]:
    ans.append((i+2,i+1))
print(len(ans))
for i in ans:
  print(i[0],i[1])