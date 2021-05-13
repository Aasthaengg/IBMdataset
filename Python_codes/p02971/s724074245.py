n=int(input())
a=[int(input()) for i in range(n)]
l=[0]*n
r=[0]*n
t=0
for i in range(n):
  t=max(t,a[i])
  l[i]=t
t=0
for i in range(n-1,-1,-1):
  t=max(t,a[i])
  r[i]=t
# print(l)
# print(r)
for i in range(n):
  if i==0:
    print(r[i+1])
    continue
  if i==n-1:
    print(l[i-1])
    continue
  print(max(r[i+1],l[i-1]))
