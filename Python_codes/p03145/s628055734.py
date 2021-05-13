T = list(map(int, input().split()))

T.sort()

x, y = T[:2]
print(x * y // 2)