st = list(input().split())
ab = list(map(int, input().split()))
d = dict(zip(st, ab))
u = input()
d[u] -= 1
print(*list(d.values()))