import sys
input = sys.stdin.readline
N=int(input())
X,Y=1,1
for i in range(N):
  T,A=map(int,input().split())
  k=max((X+T-1)//T,(Y+A-1)//A)
  X,Y=k*T,k*A
print(X+Y)