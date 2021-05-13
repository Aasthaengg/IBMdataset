import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append((A[i], i+1))

ans = []
for (a, n) in sorted(B):
    ans.append(n)

print(*ans)