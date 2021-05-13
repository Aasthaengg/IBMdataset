N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
ans = 0
for i in range(N):
    if S.count(S[i]) > T.count(S[i]):
        ans = max(ans, S.count(S[i]) - T.count(S[i]))
print(ans)