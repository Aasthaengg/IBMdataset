x, a, b = map(int, input().split())

dist1 = abs(x-a)
dist2 = abs(x-b)

if dist1 > dist2:
    print('B')
else:
    print('A')
