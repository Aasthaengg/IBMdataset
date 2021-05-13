S = input()
snx = S.replace('x', '')
ls = len(S)
if ls == 1 or len(snx) == 0:
    print(0)
    exit(0)
l = 0
r = ls-1

ans = 0
while l < r:
    lxc = 0
    while S[l] == 'x':
        l += 1
        lxc += 1
    rxc = 0
    while S[r] == 'x':
        r -= 1
        rxc += 1
    ans += abs(lxc-rxc)

    if S[l] == S[r]:
        l += 1
        r -= 1
    else:
        print(-1)
        break
else:
    print(ans)