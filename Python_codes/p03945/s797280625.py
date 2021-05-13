S = input()
now = S[0]
ans = 0
for i in range(len(S)):
    if now != S[i]:
        ans += 1
        now = S[i]
print(ans)