n, k = map(int, input().split())
p = list(map(int, input().split()))
l = [(i + 1) / 2 for i in p]
now = ans = sum(l[:k])

for i in range(1, n - k + 1):
    now += l[i + k - 1] - l[i - 1]
    ans = max(ans, now)

print(ans)