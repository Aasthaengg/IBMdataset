s = input()

ans = 0
l = len(s)
for i in range(2**(l-1)):
    ss = ''
    for j in range(l):
        ss += s[j]
        if (i >> j) & 1:
            ss += '+'
    ans += eval(ss)
print(ans)