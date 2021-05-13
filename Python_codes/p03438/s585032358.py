N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
plus=0
minus=0
gomi=0
for i in range(N):
  if(a[i]-b[i]<0):
    minus+=((b[i]-a[i])//2)*2
  else:
    plus+=a[i]-b[i]
if(minus>=plus*2):
  print("Yes")
else:
  print("No")