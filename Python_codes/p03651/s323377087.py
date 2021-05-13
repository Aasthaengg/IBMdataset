from fractions import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k > max(a):
    ans = "IMPOSSIBLE"

else:
    g = a[0]
    for e in a:
        g = gcd(g, e)

    if (max(a) - k) % g == 0:
        ans = "POSSIBLE"
    else:
        ans = "IMPOSSIBLE"

print(ans)
