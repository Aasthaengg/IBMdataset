import math

def main():
    N = int(input())
    X = tuple(map(int, input().split()))
    Y = tuple(map(int, input().split()))

    for i in (1, 2, 3):
        print(dist(X, Y, N, i))
    max_ = -float('inf')
    for i in range(N):
        max_ = max(max_, abs(X[i] - Y[i]))
    print(max_)

def dist(x, y, n, p):
    ret = 0
    for i in range(n):
        ret += abs(x[i] - y[i]) ** p
    return round(math.pow(ret, 1 / p), 6)
    
main()