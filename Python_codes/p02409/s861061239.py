n = int(input())

arrey = [[[0 for r in range(10)]for f in range(3)]for b in range(4)]

for i in range(n):
    b, f, r, v = [int(j) for j in input().split()]
    arrey[b-1][f-1][r-1] = arrey[b-1][f-1][r-1] + v

for b in range(len(arrey)):
    for f in range(len(arrey[b])):
        for r in range(len(arrey[b][f])):
            print(' ' + str(arrey[b][f][r]),end='') if r != len(arrey[b][f]) - 1 else print(' ' + str(arrey[b][f][r]))
    if b != len(arrey) - 1:
        print('####################')