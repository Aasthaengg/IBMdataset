n,m = map(int,input().split())
ans = 0
if 2*n <= m:
    ans += n
    m -= 2*n
    if m >= 4:
        ans += m//4
else:
    ans += m//2
print(ans)
