from sys import stdin
input = stdin.readline

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

z = []
w = []

for x, y in xy:
    z.append(x + y)
    w.append(x - y)

ans = max(max(z) - min(z), max(w) - min(w))

print(ans)
