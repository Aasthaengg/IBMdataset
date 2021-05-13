from itertools import product
n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]

ans = 0
for x, y, z in product([1, -1], repeat=3):
    tmp = [x * a + y * b + z * c for a, b, c in s]
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:m]))

print(ans)
