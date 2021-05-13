s = list(input())
l = len(s)
s.append("?")
ans = 0
w = "!"
x = 0
for i in range(l):
    if x == 1:
        x = 0
    elif s[i] == w:
        ans += 1
        x = 1
        w = s[i] + s[i + 1]
        if i == l - 1:
            ans -= 1
    else:
        ans += 1
        w = s[i]
print(ans)