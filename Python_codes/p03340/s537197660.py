n = int(input())
a = list(map(int, input().split()))

r = 0
s = 0

ans = 0
for l in range(n):
    while r < n and not (s & a[r]):
        s ^= a[r]
        r += 1
    ans += r - l
    s ^= a[l]

print(ans)
