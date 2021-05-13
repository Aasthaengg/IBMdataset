S = input()

ans = "NO"
for i in range(len(S)):
    for j in range(i, len(S)):
        s = S[:i] + S[j:]
        if s == "keyence":
            ans = "YES"

print(ans)
