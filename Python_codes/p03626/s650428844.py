n = int(input())
s = [input() for _ in range(2)]
ans = 1
pre_vertical = False
start = 1
flag = False
if s[0][0] == s[1][0]:
    pre_vertical = True
    ans *= 3
else:
    start = 2
    ans *= 6
for i in range(start, n):
    if flag:
        flag = False
        continue
    if s[0][i] == s[1][i]:
        if pre_vertical:
            ans *= 2
        else:
            ans *= 1
        pre_vertical = True
    else:
        if pre_vertical:
            ans *= 2
        else:
            ans *= 3
        pre_vertical = False
        flag = True
    ans %= 1000000007
print(ans)