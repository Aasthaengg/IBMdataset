S = input()
S = S.replace("BC", "D")

S = list(S)

cnt1 = 0
cnt2 = 0
ans = 0
for i in range(len(S)):
    if S[i] == "A":
        cnt1 += 1
    elif S[i] == "D":
        cnt2 += 1
        ans += cnt1
    else:
        cnt1 = 0
        cnt2 = 0
print(ans)
