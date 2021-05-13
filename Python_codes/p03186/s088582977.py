a,b,c = map(int,input().split())
ans = 0
if a+b <= c:
    ans += a+b
    if ans == c:
        ans += b
    elif ans < c:
        ans += b+1
else:
    ans += b+c
print(ans)
