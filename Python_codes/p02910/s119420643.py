s = input()
l = len(s)
o = ["R", "U", "D"]
e = ["L", "U", "D"]
x = 1
for i in range(l):
    if i == (2 * int(i / 2)):
        if s[i] not in o:
            x = 0
    else:
        if s[i] not in e:
            x = 0
print("Yes" if x == 1 else "No")