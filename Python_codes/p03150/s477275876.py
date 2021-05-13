s = input()
f = False
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[:i]+s[j:] == "keyence":
            f = True
print("YES" if f else "NO")