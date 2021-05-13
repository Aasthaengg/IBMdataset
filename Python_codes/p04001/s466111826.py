s = input()
l = len(s)

ans = 0

for i in range(2**(l-1)):
    a = s[0]
    for j in range(l-1):
        if i >> j & 1 == 1:
            a += '+'
        a += s[j+1]
    ans += eval(a)
print(ans)