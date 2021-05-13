# A - Maximize the Formula

A, B, C = map(int, input().split())

ans = 0

ans = max(ans, A*10+B+C)
ans = max(ans, A+B*10+C)
ans = max(ans, A+B+C*10)

print(ans)