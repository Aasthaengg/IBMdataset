import sys

input = sys.stdin.readline
N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N-1):
    if x < A[i]:
        break
    x -= A[i]
    ans += 1
if A[-1] == x:
    ans += 1

print(ans)