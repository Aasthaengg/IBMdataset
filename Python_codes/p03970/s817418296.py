S = list(input())
s = list("CODEFESTIVAL2016")

ans = 0
for i in range(len(S)):
    if S[i] != s[i]:
        ans += 1

print(ans)