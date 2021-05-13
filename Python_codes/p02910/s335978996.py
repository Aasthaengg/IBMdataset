s = str(input())
count = 0
a = ["R", "U", "D"]
b = ["L", "U", "D"]
for i in s[::2]:
    if i in a:
        pass
    else:
        count = 1
        break
for i in s[1::2]:
    if i in b:
        pass
    else:
        count = 1
        break
print("Yes" if count == 0 else "No")