a = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())

for i in range(n):
    b, f, r, v = [int(i) for i in input().split()]
    a[b-1][f-1][r-1] += v

for i, x in enumerate(a):
    for y in x:
        for z in y:
            print(' %d' % z, end='')
        print('')
    if i < 4 - 1:
        print('####################')