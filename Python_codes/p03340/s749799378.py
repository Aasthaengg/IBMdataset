n = int(input())
a = [int(x) for x in input().split()]
ans = 0
s = 0
x = 0
r = 0
for l in range(n):
    while r<n and s+a[r]==x^a[r]:
        s += a[r]
        x ^= a[r]
        r += 1
    ans += (r-l)
    if l==r:
        r += 1
    else:
        s -= a[l]
        x ^= a[l]
print(ans)