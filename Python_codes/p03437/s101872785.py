import sys
x,y=map(int,input().split())
k=0
if x%y==0 or x*(y-1)>10**18:
    print(-1)
else:
    print(x*(y-1))