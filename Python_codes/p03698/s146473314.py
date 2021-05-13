s = input()
chk = []
for i in range(len(s)):
    c = s[i]
    if c in chk:
        print("no")
        exit()
    else:
        chk.append(c)
print("yes")