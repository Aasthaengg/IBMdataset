a, b = map(int, input().split())
k = (a + b) // 2
if abs(k - a) == abs(k - b):
    print(k)
else:
    print('IMPOSSIBLE')