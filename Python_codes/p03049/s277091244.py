n = int(input())
S = [input() for i in range(n)]

ans = 0
a = 0
b = 0
c = 0
for i in range(n):
    for j in range(len(S[i]) - 1):
        if S[i][j:j+2] == "AB":
            ans += 1
    if S[i][-1] == "A":
        a += 1
    if S[i][0] == "B":
        b += 1
    if S[i][-1] == "A" and S[i][0] == "B":
        c += 1
# print(ans)
ans += min(a, b)
if a == c and a == b and a > 0:
    ans -= 1

print(ans)