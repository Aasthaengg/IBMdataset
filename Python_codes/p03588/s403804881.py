n=int(input())
amax=0
bmax=0
amin=1000
bmin=1000
for i in range(n):
  a,b=map(int,input().split())
  if a>amax:
    amax=a
    bmax=b      

print(amax+bmax)