from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

AA=[0]*N
AA[0]=A[0]
c=0
for i in range(1,N):
  if A[i]>=AA[i-1]:AA[i]=A[i]
  else:AA[i]=AA[i-1]
  c=c+AA[i]-A[i]
print(c)