n=int(input())
h=list(map(int,input().split()))
ans=0
temp=[0]*n
while True:
  a=0
  b=1
  cnt=1
  for i in range(n):
    if h[i]!=temp[i]:
      temp[i]=temp[i]+1
      a=1
      b=0
    elif a==1:
      cnt=cnt+1
      a=0
      b=1
  if b==1:
    cnt=cnt-1
  ans=ans+cnt
  if sum(temp)==sum(h):
    break
print(ans)