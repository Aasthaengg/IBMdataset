import sys
input=lambda: sys.stdin.readline().rstrip()
n=int(input())
A,B=[],[]
for _ in range(n):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
A.sort()
B.sort()
if n%2==1:
  l=A[n//2]
  r=B[n//2]
  print(r-l+1)
else:
  l=A[n//2-1]+A[n//2]
  r=B[n//2-1]+B[n//2]
  print(r-l+1)
