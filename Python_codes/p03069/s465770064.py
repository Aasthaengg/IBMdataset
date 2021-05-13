N = int(input())
S = input().strip()

bcnt = S.count("#")
wcnt = N - bcnt

ans = wcnt
cntb = 0
cntw = 0
for i in range(N):
    if S[i] == "#":
        cntb += 1
    else:
        cntw += 1

    ans = min(ans, cntb + wcnt - cntw)


print(ans)

