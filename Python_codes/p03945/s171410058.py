S = list(input())
ls = len(S)
p = S[0]
ans = 0
for i in range(1, ls):
    if S[i] != p:
        ans += 1
        p = S[i]
print(ans)