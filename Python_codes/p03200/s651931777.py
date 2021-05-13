S = list(input())
N = len(S)
ans = 0

WWW = S.count("W")

for i in range(N):
    if S[i] == "B":
        ans += WWW
    if S[i] == "W":
        WWW -= 1

print(ans)
