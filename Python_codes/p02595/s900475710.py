N, D = map(int, input().split())
ans = 0
D2 = D**2
for _ in range(N):
    X, Y = map(int, input().split())
    if X**2 + Y**2 <= D2:
        ans += 1
print(ans)