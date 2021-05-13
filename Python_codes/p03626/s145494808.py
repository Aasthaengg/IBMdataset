#dekimasen-deshita-
n = int(input())
s = [input(), input()]
mod = 10**9+7
i = 0
ans = 3
pre = 0

while i < n:
    if s[0][i] == s[1][i]:
        typ = 1
        i += 1
    else:
        typ = 2
        i += 2
    if pre == 0 and typ == 2:
        ans *= 2
    elif pre == 1:
        ans = (ans*2)%mod
    elif pre == 2 and typ == 2:
        ans = (ans*3)%mod
    pre = typ
print(ans)