from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()
b=lnii()

plus=[]
minus=0
ans=0
for i in range(n):
  if a[i]<b[i]:
    minus+=b[i]-a[i]
    ans+=1
  else:
    plus.append(a[i]-b[i])

if minus==0:
  print(0)
  exit()

plus.sort(reverse=True)
for i in range(len(plus)):
  minus-=plus[i]
  ans+=1
  if minus<=0:
    print(ans)
    exit()

print(-1)