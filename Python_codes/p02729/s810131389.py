import itertools
n, m = map(int, input().split())

nn = []
i = 0
for _ in range(n):
    nn.append(i)
    i += 2

mm = []
i = 1
for _ in range(m):
    mm.append(i)
    i += 2

ans = 0
l = nn + mm

for v in itertools.combinations(l, 2):
    if (v[0] + v[1]) % 2 == 0:
        ans += 1
print(ans)
