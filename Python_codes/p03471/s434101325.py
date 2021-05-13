N, Y = map(int, input().split())

b = 0
for x in range(N+1):
    if b == 1:
        break
    for y in range(N+1-x):
        z = N - (x + y)
        if x*10000 + y*5000 + z*1000 == Y:
            print(x, y, z)
            b += 1
            break
if b == 0:
    print('-1 -1 -1')
