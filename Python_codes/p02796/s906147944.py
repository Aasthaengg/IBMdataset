N = int(input())
xl = [list(map(int, input().split())) for _ in range(N)]

xl.sort()

ans = N
rpre = xl[0][0] + xl[0][1]

for x, l in xl[1:]:
    ll = max(x - l, 0)
    rr = x + l
    if ll < rpre:
        ans -= 1
        if rr < rpre: rpre = rr
    else:
        rpre = rr

print(ans)
