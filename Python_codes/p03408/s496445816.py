n=int(input())
a={}
for _ in range(n):
  s=input()
  if a.get(s):a[s]+=1
  else:a[s]=1
m=int(input())
b={}
for _ in range(m):
  s=input()
  if b.get(s):b[s]+=1
  else:b[s]=1
ans=0
for i in a:
  ans=max(a[i]-b.get(i,0),ans)
print(ans)