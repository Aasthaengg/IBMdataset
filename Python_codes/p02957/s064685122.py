a, b = map(int, input().split())
ans = (abs(a - b) // 2) + min(a, b)
print(ans if abs(a - b) % 2 == 0 else "IMPOSSIBLE")