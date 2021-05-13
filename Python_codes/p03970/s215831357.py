S = input()
ans = 0
chk = "CODEFESTIVAL2016"
for i, s in enumerate(S):
    if s != chk[i]:
        ans += 1
print(ans)