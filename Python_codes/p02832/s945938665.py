import sys
input = sys.stdin.readline

N=int(input().rstrip('\n'))
A=[int(x) for x in input().rstrip('\n').split()]
now = 0
for x in range(N):
  if A[x] == now+1:
    now += 1
if now == 0:
  print(-1)
else:
  print(N-now)