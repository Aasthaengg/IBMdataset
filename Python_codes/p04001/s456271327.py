s = input()
n = len(s)
ans = 0
for i in range(2 ** (n-1)):
    tmp = []
    for k in range(n-1):
        tmp.append(s[k])
        if i>>k & 1:
            tmp.append("+")
    tmp.append(s[-1])
    ans += eval("".join(tmp))
print(ans)