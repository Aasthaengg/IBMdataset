n,m=map(int, input().split())
alist=[0]*(n+10)
for i in range(m):
  alist[int(input())]=-1
ans=True
alist[0]=1
for i in range(n):
  if alist[i]!=-1:
    if alist[i+1]!=-1 and alist[i+2]!=-1:
      alist[i+1]+=alist[i]
      alist[i+2]+=alist[i]
    elif alist[i+2]!=-1:
      alist[i+2]+=alist[i]
    elif alist[i+1]!=-1:
      alist[i+1]+=alist[i]
    else:
      ans=False
if ans:
  print(alist[n]%(10**9+7))
else:
  print(0)