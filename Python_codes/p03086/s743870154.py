S = input()

ans = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        ok = True
        for k in range(i, j+1):
            if not (S[k] == "A" or S[k] == "C" or S[k] == "G" or S[k] == "T"):
                ok = False
                break
        if ok:
            ans = max(ans, j - i + 1)

print(ans)
