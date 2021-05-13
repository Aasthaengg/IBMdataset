n = int(input())
S = [input() for _ in range(n)]
m = int(input())
T = [input() for _ in range(m)]

ans = 0
for s in S:
    rwd = 0
    for i in range(n):
        if s == S[i]:
            rwd += 1
    for i in range(m):
        if s == T[i]:
            rwd -= 1
    ans = max(rwd, ans)
print(ans)