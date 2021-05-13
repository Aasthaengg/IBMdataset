# https://atcoder.jp/contests/abc103/tasks/abc103_d

N, M = map(int, input().split())
AB = []
for _ in range(M):
    ai, bi = map(int, input().split())
    AB.append((ai, bi))
AB = sorted(AB, key=lambda x: x[1])

ans, x = 0, 0

for (a, b) in AB:
    if a > x:
        ans += 1
        x = b - 1
print(ans)