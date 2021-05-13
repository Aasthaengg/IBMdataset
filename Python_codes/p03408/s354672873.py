n = int(input())
S = [input() for _ in range(n)]
m = int(input())
T = [input() for _ in range(m)]
ans = 0
for i in S:
    p = S.count(i)
    m = T.count(i)
    ans = max(ans, p - m)
print(ans)