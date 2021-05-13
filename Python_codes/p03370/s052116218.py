N, X = map(int, input().split())
m = []
for _ in range(N):
    m.append(int(input()))

rem = X - sum(m)
ans = N + rem//min(m)
print(ans)