import itertools
n, k = map(int, input().split())
max_val = (n - 1) * (n - 2) // 2
if max_val < k:
    print(-1)
    quit()
m = max_val - k

print (n - 1 + m)
for i in range(2, n + 1):
    print("{} {}".format(1, i))

for i, j in itertools.combinations(range(2, n + 1), 2):
    if m == 0:
        break
    print("{} {}".format(i, j))
    m -= 1