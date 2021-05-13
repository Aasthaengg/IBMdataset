n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]
st, stx, sty = 0, 0, 0
ans = "Yes"
for t, x, y in txy:
    ta, xa, ya = abs(t - st), abs(x - stx), abs(y - sty)
    if ta >= xa + ya and (
        (ta % 2 == 1 and (xa + ya) % 2 == 1) or (ta % 2 == 0 and (xa + ya) % 2 == 0)
    ):
        st, stx, sty = t, x, y
    else:
        ans = "No"
        break
print(ans)
