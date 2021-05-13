x, a, b = map(int, input().split())
la = abs(x-a)
lb = abs(x-b)
if la < lb:
    print('A')
else:
    print('B')