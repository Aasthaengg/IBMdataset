university = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    university[b - 1][f - 1][r - 1] += v
c1 = c2 = 0
for building  in university:
    c2 = 0
    for floor in building:
        for room in floor:
            print(' {}'.format(room), end = '')
        if c2 != 2:
            print('')
        c2 += 1
    if c1 != 3:
        print('\n####################')
    c1 += 1
print('')

