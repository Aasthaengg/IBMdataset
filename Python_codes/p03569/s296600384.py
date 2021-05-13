S = input()
N = len(S)
l, r = 0, N-1
flg = 1
while l < r:
    while l < r and S[l] == 'x':
        l += 1
    while r > l and S[r] == 'x':
        r -= 1
    if S[l] != S[r]:
        flg = 0
        break
    l += 1
    r -= 1
if flg == 0:
    print(-1)
    exit()
l, r = 0, N-1
ans = 0
while l < r:
    if S[l] != S[r]:
        if S[l] == 'x':
            l += 1
        else:
            r -= 1
        ans += 1
    else:
        l += 1
        r -= 1
print(ans)