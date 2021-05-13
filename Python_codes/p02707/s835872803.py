N = int(input())
import sys
input = sys.stdin.readline
lis = {}
A = list(map(int, input().split()))
for i in range(N-1):
  x = A[i]
  if x in lis:
    lis[x] += 1
  else:
    lis[x] = 1
for i in range(1, N+1):
  if lis.get(i) == None:
    print(0)
  else:
    print(lis.get(i))