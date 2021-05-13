s = input()
g = 0
p = 0
ans = 0
for i in s:
    if g == p:
        g += 1
        if i == "p":
            ans -= 1
    else:
        p += 1
        if i == "g":
            ans += 1
print(ans)