s = input()

res = False
for i in range(len(s)+1):
    for j in range(i, len(s)+1):
        if (s[:i] + s[j:]) == "keyence":
            res = True
            break

print("YES" if res else "NO")