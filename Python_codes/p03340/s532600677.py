n = int(input())
a = list(map(int, input().split()))
m, x, c = 0, 0, 0
j = 0
ans = 0
for i in range(n):
    m += a[i]
    x ^= a[i]
    c += 1
    if not m == x:
        while True:
            if m == x:
                break
            x ^= a[j]
            m -= a[j]
            j += 1
            c -= 1
    ans += c
print(ans)