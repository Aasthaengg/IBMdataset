N, Y = map(int, input().split())

for ykt in range(0, N+1):
    for icy in range(0, N+1):
        hdy = N - ykt - icy
        if hdy < 0:
            continue
        if 10000 * ykt + 5000 * icy + 1000 * hdy == Y:
            print(str(ykt) + ' ' + str(icy) + ' ' + str(hdy))
            exit()

print('-1 -1 -1')