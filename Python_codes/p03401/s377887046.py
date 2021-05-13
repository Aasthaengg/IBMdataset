N = int(input())
coordinate = [0]
coordinate = coordinate + list(map(int, input().split()))
coordinate.append(0)
summ = 0

for i in range(N + 1):
    summ += abs(coordinate[i + 1] - coordinate[i])

diff_coorinate = []

for i in range(N):
    distance = abs(coordinate[i + 2] - coordinate[i])
    diff_coorinate.append(distance)

for i in range(N):

    next = coordinate[i + 1] - coordinate[i]
    n_next = coordinate[i + 2] - coordinate[i + 1]
    
    if (next * n_next >= 0):
        ans = summ
    elif (coordinate[i + 2] - coordinate[i] >= 0):
        d = abs(min(next, n_next))
        ans = summ - 2 * d
    else:
        d = max(next, n_next)
        ans = summ - 2 * d
    
    print(ans)
