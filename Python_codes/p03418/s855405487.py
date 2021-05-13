n,k = map(int,input().split())

if k == 0:
    print(n*n)
    import sys
    sys.exit()

ans = 0
for i in range(k+1,n+1):
    a = n // i
    ans += (i-k) * a
    if k <= n % i and n % i != 0:
        ans += n % i - k + 1
print(ans)

