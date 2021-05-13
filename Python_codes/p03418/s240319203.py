n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    #print(i, n-(n//i)*i - k )
    ans += max(0, n//i * (i-k))
    ans += max((n-(n//i)*i) - k + 1, 0)

if k == 0:
    print(n*n)
else:
    print(ans)
