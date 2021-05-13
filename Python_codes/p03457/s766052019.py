import sys
n=int(input())
currtime=0
currx=0
curry=0
for i in range(n):
  t,x,y=map(int,input().split())
  if abs(y-curry)+abs(x-currx)<=t-currtime and (abs(y-curry)+abs(x-currx))%2==(t-currtime)%2:
    currx=x
    curry=y
    currtime=t
  else:
    print('No')
    sys.exit()
print('Yes')