import sys
a,b,k=map(int,input().split())
for i in range(1,101):
  if a%(101-i)==0 and b%(101-i)==0:
    k-=1
  if k==0:
    print(101-i)
    sys.exit()