n, k = [ int(v) for v in input().split() ]

if k == 0:
    ans = n ** 2
else:
    ans = 0
    for i in range(k+1,n+1):
        j = n - k + 1
        a, b = j // i, j % i
        ans += a * (i-k) + min(b, i-k)
print(ans)
