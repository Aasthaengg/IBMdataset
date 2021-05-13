import sys
input=lambda: sys.stdin.readline().rstrip()
n,k=map(int,input().split())
A=[int(i) for i in input().split()]
for i in range(k,n):
  if A[i]>A[i-k]:
    print("Yes")
  else:
    print("No")