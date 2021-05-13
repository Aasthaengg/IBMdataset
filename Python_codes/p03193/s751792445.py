n, tate, yoko = map(int, input().split())
ans = 0
for _ in range(n):
    Y, X = map(int, input().split())
    if Y >= tate and X >= yoko: ans += 1
print(ans)
