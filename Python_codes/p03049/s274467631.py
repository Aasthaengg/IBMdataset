n = int(input())

ans = 0

BA = 0
XA = 0
BX = 0

for i in range(n):
    s = input()
    ans += s.count('AB')

    if s[0] == 'B' and s[-1] == 'A':
        BA += 1
    elif s[-1] == 'A':
        XA += 1
    elif s[0] == 'B':
        BX += 1

if BA > 0:
    ans += BA-1
    BA = 1
    if BX > 0:
        ans += 1
        BA = 0
    else:
        BX = 1
        BA = 0

ans += min(XA, BX)

print(ans)
