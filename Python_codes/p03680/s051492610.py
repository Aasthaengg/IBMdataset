n=int(input())
a=[int(input()) for _ in range(n)]

a0=a[0]
cnt=0
f=True

if a0==2:
  cnt=1
  f=False

for i in range(n):
  if f:
    a0=a[a0-1]
    cnt+=1
    if a0 == 2:
      cnt+=1
      break

if cnt==n:
  cnt=-1

print(cnt)