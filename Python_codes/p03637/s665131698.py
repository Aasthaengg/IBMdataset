import sys
N=int(input())
A=list(map(int,input().split()))
a=len([i for i in A if i%4==0])
b=len([i for i in A if i%4==2])
if b==0:
  if a*2+1>=N:
    print("Yes")
    sys.exit()
  else:
    print("No")
    sys.exit()
if a*2+b>=N:
  print("Yes")
else:
  print("No")