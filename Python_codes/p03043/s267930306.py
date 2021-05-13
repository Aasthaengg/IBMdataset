from math import ceil

n, k = map(int, input().split())

bef = n + 1
ans = 0
div = 1
while k > 0.5:
    a = ceil(k)
    cnt = max(0, bef - a)
    ans += cnt * div
    div /= 2
    k /= 2
    bef = min(n + 1, a)
print(ans / n)