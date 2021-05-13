n,m = map(int,input().split())

m //= 2

ans = 0

if n <= m:
    ans += n
    m -= n
    ans += (m//2)
    print(ans)
else:
    ans = m
    print(ans)