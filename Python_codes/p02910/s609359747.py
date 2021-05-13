s = input()
flg = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in ["R", "U", "D"]:
            flg = 1
    else:
        if s[i] not in ["L", "U", "D"]:
            flg = 1
print("Yes" if flg == 0 else "No")