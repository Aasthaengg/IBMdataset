S=input()
ans = 0
for i, x in enumerate("CODEFESTIVAL2016"):
    if S[i] != x:
        ans += 1
print(ans)
