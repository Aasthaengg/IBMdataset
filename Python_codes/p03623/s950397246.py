x, a, b = map(int, input().split())

distA = abs(x-a)
distB = abs(x-b)

if distA < distB:
    print('A')
else:
    print('B')