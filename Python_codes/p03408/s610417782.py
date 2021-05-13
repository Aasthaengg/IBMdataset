n = int(input())
S = list(input() for _ in range(n))
m = int(input())
T = list(input() for _ in range(m))
ans = 0
for i in list(set(S)):
    ans = max(ans, S.count(i) - T.count(i))
print(ans)