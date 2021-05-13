s = input()
n = len(s)
ans = 0
for i in range(2**(n-1)):
    x = []
    for j in range(n):
        x.append(s[j])
        if (i>>j) & 1:
            y = int("".join(x))
            ans += y
            x = []
        else:
            pass
    if x != []:
        y = int("".join(x))
        ans += y
print(ans)