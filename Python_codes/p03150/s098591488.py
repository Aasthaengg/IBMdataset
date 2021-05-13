s = input()
for i in range(8):
    if s[:i] + s[i+len(s)-7:] == "keyence":
        print("YES")
        exit()
print("NO")