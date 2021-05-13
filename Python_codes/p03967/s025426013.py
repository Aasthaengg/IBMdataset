s = input()
n = len(s)
nowp = 0
nowg = 0
ans = 0

for i in range(n):
    if s[i] == "g":
        if nowp < nowg:
            nowp += 1
            ans += 1
        elif nowp == nowg:
            nowg += 1
    elif s[i] == "p":
        if nowp < nowg:
            nowp += 1
        elif nowp == nowg:
            nowg += 1
            ans -= 1
print(ans)