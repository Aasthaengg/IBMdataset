from collections import defaultdict

n = int(input())
ns = defaultdict(int)

for i in range(1, n + 1):
    ns[(str(i)[0], str(i)[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += ns[(str(i), str(j))] * ns[(str(j), str(i))]
print(ans)
