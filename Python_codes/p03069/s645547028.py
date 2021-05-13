import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input().rstrip()

lb = [0] * (N+1)
for i, c in enumerate(S, 1):
    lb[i] = lb[i-1] + (1 if c=='#' else 0)

ans = N + 100
bl = lb[-1]
for i in range(N+1):
    j = i+1
    left = lb[i]
    right = N - i - (bl - lb[i])
    ans = min(ans, left+right)
print(ans)

