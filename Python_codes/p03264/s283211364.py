import itertools
k = int(input())
p = []
for i in range(1, k+1):
    p.append(i)
ans = 0
for v in itertools.combinations(p, 2):
    if v[0] % 2 == 0 and v[1] % 2 == 1 or v[1] % 2 == 0 and v[0] % 2 == 1:
        ans += 1
print(ans)
