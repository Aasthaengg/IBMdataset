a = list(map(int, input().split()))
a.sort()
d = a[2] - a[1]
a[0] += d
ans = d + (a[2] - a[0]) // 2
if (a[0] ^ a[2]) & 1:
    ans += 2
print(ans)
