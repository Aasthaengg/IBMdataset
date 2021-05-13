import itertools

n, x, y = map(int, input().split())
x -= 1
y -= 1
ans = [0 for _ in range(n - 1)]
for i, j in itertools.combinations(range(n), 2):
    d = min(abs(i - j), abs(i - x) + abs(j - y) + 1, abs(i - y) + abs(j - x) + 1)
    ans[d - 1] += 1
for num in ans:
    print(num)