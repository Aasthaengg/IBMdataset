inf = int(9e18)


def recursive(i, total, cost, C, A, X):
    if i == len(A):
        return inf
    ncost = recursive(i+1, total, cost, C, A, X)

    ok = True
    for j in (range(len(total))):
        total[j] += A[i][j]
        if (total[j] < X):
            ok = False
    if ok:
        dcost = cost + C[i]
    else:
        dcost = recursive(i+1, total, cost + C[i], C, A, X)
    for j in (range(len(total))):
        total[j] -= A[i][j]

    return (min(ncost, dcost))


def main():
    nmx = [int(_x) for _x in input().split()]
    n = nmx[0]
    m = nmx[1]
    x = nmx[2]
    c = []
    a = []
    for i in range(n):
        ca = [int(_x) for _x in input().split()]
        c.append(ca[0])
        a.append(ca[1:])
    total = [0] * m

    result = recursive(0, total, 0, c, a, x)

    if result == inf:
        print(-1)
    else:
        print(result)


main()
