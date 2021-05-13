N, K, Q = map(int, input().split())
import sys
input = sys.stdin.readline
A = [0] * N
for i in range(Q):
  s = int(input().rstrip())
  A[s-1] += 1
for k in A:
  if K - (Q - k) >= 1:
    print("Yes")
  else:
    print("No")