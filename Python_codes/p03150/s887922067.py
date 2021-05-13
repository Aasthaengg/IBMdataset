s = input()
ans = 0
for i in range(len(s)):
    for j in range(len(s)):
        t = s[:i] + s[j:]
        if t == "keyence":
            ans = 1
            break
if ans == 1:
    print("YES")
else:
    print("NO")