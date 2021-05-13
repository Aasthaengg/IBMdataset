s = sum(map(int, input().split()))
print('IMPOSSIBLE' if s % 2 else s // 2)
