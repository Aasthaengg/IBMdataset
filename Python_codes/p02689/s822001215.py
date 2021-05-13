n, m = map(int, input().split())
h = [0] + list(map(int, input().split()))
ok = [0] + [1 for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    if h[a] <= h[b]:
        ok[a] = 0
    if h[b] <= h[a]:
        ok[b] = 0

print(sum(ok))