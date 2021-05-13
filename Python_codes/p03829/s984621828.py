def resolve():
    N, A, B = list(map(int, input().split()))
    X = list(map(int, input().split()))
    point = 0
    for i in range(1, N):
        if abs(X[i]-X[i-1])*A < B:
            point += abs(X[i]-X[i-1])*A
        else:
            point += B
    print(point)


if __name__ == '__main__':
    resolve()