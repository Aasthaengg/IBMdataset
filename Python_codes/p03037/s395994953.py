n, m = map(int, input().split())
l = []
r = []
for i in range(m):
    L, R = map(int, input().split())
    l += [L]
    r += [R]

l_max = max(l)
r_min = min(r)

print(max(r_min - l_max + 1, 0))