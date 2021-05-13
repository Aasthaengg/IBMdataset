

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    n, m = read_ints()
    X = read_ints()
    Y = read_ints()
    areaX = [0]*n
    modulo = 10**9+7
    for i in range(1, len(X)):
        areaX[i] = (areaX[i-1]+i*(X[i]-X[i-1]))%modulo
    areaY = [0]*m
    for i in range(1, len(Y)):
        areaY[i] = (areaY[i-1]+i*(Y[i]-Y[i-1]))%modulo
    return (sum(areaX)*sum(areaY))%modulo


if __name__ == '__main__':
    print(solve())
