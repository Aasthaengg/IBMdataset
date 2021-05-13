N=int(input())
X,Y=map(int,input().split())
T,A=0,0
b,c=0,0
for i in range(N-1):
  T,A=map(int,input().split())
  b=((X+T-1)//T)*T
  c=(b//T)*A
  if c>=Y:
    X,Y=b,c
  else:
    Y=((Y+A-1)//A)*A
    X=(Y//A)*T
print(X+Y)