N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

ans = 0
P = set(S)
for i in P:
    ans = max(ans,S.count(i)-T.count(i))

print(ans)
