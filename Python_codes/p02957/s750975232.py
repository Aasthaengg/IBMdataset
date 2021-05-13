A, B = map(int, input().split())
print('IMPOSSIBLE' if abs(A-B) % 2 != 0 else int(min(A, B) + (abs(A-B) / 2)))