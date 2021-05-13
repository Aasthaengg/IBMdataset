a,b = map(int, input().split())
ans = 0
if a>b:
    ans += a
    if a-1 > b:
        ans += a-1
    else:
        ans += b
else:
    ans += b
    if b-1 > a:
        ans += b-1
    else:
        ans += a
print(ans)