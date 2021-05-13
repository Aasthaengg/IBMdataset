x, a, b = map(int, input().split())
i = abs(x-a)
j = abs(x-b)
if i < j:
    print('A')
else:
    print('B')
