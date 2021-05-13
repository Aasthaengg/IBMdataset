s = input()
S = []
xid = [0] * (10 ** 5 + 1)
xcnt = 0
for c in s:
    if c != "x":
        S.append(c)
        xcnt += 1
    else:
        xid[xcnt] += 1
xid = xid[:xcnt + 1]
ans = 0
if S[0:xcnt // 2] == S[-1:-(xcnt // 2) - 1:-1]:
    for i in range(-(-xcnt // 2)):
        ad = xid[i] - xid[xcnt - i]
        if ad < 0:
            ad = -ad
        ans += ad
    print(ans)
else:
    print(-1)