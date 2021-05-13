N, Y = map(int, input().split())
count = 0

for i in range(N+1):
    if count == 1:
        break
    else:
        for j in range(N+1-i):
            k = N - (i + j)
            if 10000 * i + 5000 * j + 1000 * k == Y:
                count += 1
                print('{} {} {}'.format(i, j, k))
if count == 0:
    print('-1 -1 -1')