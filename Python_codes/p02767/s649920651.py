N = int(input())
X = tuple(map(int, input().split()))
ans = 10 ** 7
for p in range(min(X), max(X) + 1):
    total = 0
    for x in X:
        total += (x - p) ** 2
    ans = min(ans, total)
print(ans)