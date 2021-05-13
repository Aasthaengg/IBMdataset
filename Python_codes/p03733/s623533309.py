from sys import stdin
input = stdin.readline


N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0

for i in range(N - 1):
    ans += min(T, t[i + 1] - t[i])

print(ans + T)
