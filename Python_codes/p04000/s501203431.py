import sys
input=sys.stdin.readline
h,w,n=map(int,input().split())
ans=[(h-2)*(w-2)]+[0]*9
s1=set()
s2=set()
for i in range(n):
  a,b=map(int,input().split())
  s2.add(a*(10**10)+b)
  for j in range(3):
    for k in range(3):
      if 0<a-j<h-1 and 0<b-k<w-1:
        s1.add((a-j)*(10**10)+b-k)
for x in s1:
  now=0
  for i in range(3):
    for j in range(3):
      if (x+i*(10**10)+j) in s2:
        now+=1
  ans[now]+=1
ans[0]-=sum(ans[1:])
[print(x) for x in ans]
