n, k = map(int, input().split())

if k <= n:
    if n%k == 0:
        ans = 0
    else:
        tmp = n//k
        ans = min(abs((n-k*tmp)), abs((n-(k*(tmp+1)))))
else:
    ans = min(abs(n), abs(n-k))

print(ans)