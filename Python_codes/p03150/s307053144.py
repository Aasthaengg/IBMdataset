s = input()

n = len(s)

ans = False
for i in range(n):
    for j in range(i, n):
        if s[:i] + s[j:] == "keyence":
            ans = True

print("YES" if ans else "NO")

