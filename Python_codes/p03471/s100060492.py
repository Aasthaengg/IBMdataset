N, Y = map(int, input().split())

count = 0

for x in range(N+1):
    for y in range(N+1-x):
        if 10000*x+5000*y+1000*(N-x-y) == Y:
            count += 1
            print("{} {} {}".format(x, y, N-x-y))
            if count == 1:
                break
    if count == 1:
                break

if count == 0:
    print("-1 -1 -1")