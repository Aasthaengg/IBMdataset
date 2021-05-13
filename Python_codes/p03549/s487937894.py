import sys
input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
t = 1900 * M + 100 * (N - M)
r = 1 - (1/2) ** M
ans = t * ((1/2) ** M) * (1/(1 - r) ** 2)
print(int(ans)) 