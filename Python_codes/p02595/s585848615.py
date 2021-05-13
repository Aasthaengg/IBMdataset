N, D = map(int, input().split())
Zn = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for Z in Zn:
    X, Y = Z
    if (X**2 + Y**2 <= D**2):
        ans += 1
print(ans)