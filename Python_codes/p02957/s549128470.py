a, b = map(int, input().split())
print('IMPOSSIBLE' if (b + a) % 2 else (b + a) // 2)