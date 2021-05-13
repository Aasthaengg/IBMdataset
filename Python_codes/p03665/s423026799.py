import sys
def input():
  return sys.stdin.readline().rstrip()

N,P=map(int,input().split())
A=list(map(int,input().split()))

temp=0
for i in range(N):
  if A[i]%2==1:
    temp+=1
if temp==0:
  print(1<<N if P == 0 else 0)
else:
  print(1<<(N-1))
