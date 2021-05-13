s = input()

flag = False
for i in range(len(s)):
    for j in range(i, len(s) + 1):
        if s[:i] + s[j:] == "keyence":
            flag = True

if flag:
    print("YES")
else:
    print("NO")

