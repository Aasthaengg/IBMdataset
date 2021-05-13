n = int(input())
a = list(map(int,input().split()))
ans = 0
l,r = 0, 0
xor = a[0]
add = a[0]

while r < n and l <= r:
    if xor == add:
        ans += r - l + 1
        r += 1
        if r< n:
            xor ^= a[r]
            add += a[r]
    else:
        if l < n:
            xor ^= a[l]
            add -= a[l]
        l += 1

print(ans)
