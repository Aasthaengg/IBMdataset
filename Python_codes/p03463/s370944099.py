def inpl(): return [int(i) for i in input().split()]

N, A, B = inpl()
if (A-B)%2:
    print('Borys')
else:
    print('Alice')