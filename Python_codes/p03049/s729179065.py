def count_AB(s):
    res = 0
    for j in range(len(s) - 1):
        if s[j] == 'A' and s[j + 1] == 'B':
            res += 1
    return res


N = int(input())
sA, BsA, Bs = (0, 0, 0)
ans = 0
for i in range(N):
    s = input()
    if s[0] == 'B' and s[-1] == 'A':
        BsA += 1
        if len(s[1:-1]) > 0:
            ans += count_AB(s[1:-1])
    elif s[0] == 'B':
        Bs += 1
        if len(s[1:]) > 0:
            ans += count_AB(s[1:])
    elif s[-1] == 'A':
        sA += 1
        if len(s[:-1]) > 0:
            ans += count_AB(s[:-1])
    else:
        ans += count_AB(s)

if BsA == 0:
    ans += min(sA, Bs)
else:
    if sA + Bs == 0:
        ans += BsA - 1
    else:
        ans += BsA
        ans += min(sA, Bs)

print(ans)