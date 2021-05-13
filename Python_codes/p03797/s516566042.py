S, C = map(int, input().split())

ans = min(C//2, S)
ans += (C - ans * 2) // 4

print(ans)