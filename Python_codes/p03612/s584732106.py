import sys


def input():
    return sys.stdin.readline().strip()


N = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    if i + 1 == P[i]:
        P[i], P[i + 1] = P[i + 1], P[i] 
        ans += 1
if P[N-1] == N:
    ans += 1
print(ans)
