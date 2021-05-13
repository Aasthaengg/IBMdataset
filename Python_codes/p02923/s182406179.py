import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

ans = 0
cur = 0
for i in range(1, N):
  if A[i] <= A[i - 1]:
    cur += 1
    if cur > ans:
      ans = cur
  else:
    cur = 0

print(ans)