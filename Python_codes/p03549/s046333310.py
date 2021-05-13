from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m=nii()

ms=1900*m+100*(n-m)

ans=0
for i in range(1,10**6):
  p1=0.5**m
  p2=(1-0.5**m)**(i-1)
  p=p1*p2
  t_ms=ms*i
  ans+=p*t_ms

ans=int(ans)
q=ans%10
if q!=0:
  ans+=10-q

print(ans)