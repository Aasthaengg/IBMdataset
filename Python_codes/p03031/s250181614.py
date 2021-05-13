n,m=map(int,input().split())
a=[]
ans=0
for _ in range(m):
  t=list(map(int,input().split()))
  t.pop(0)
  a.append(t)
b=list(map(int,input().split()))
for i in range(2**n):
  c=[0]*m
  for j in range(n):
     if ((i>>j) & 1):
        for k in range(len(a)):
          if (j+1) in a[k]:
            c[k]+=1
  flg=0
  for j in range(m):
    if c[j]%2!=b[j]:
      flg=1
  if flg==0:
    ans+=1
print(ans)