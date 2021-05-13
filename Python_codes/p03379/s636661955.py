def mi():
    return map(int, input().split())

def main():
    N = int(input())
    X = list(mi())
    Y = sorted(X)
    for i in range(N):
        if X[i] <= Y[N//2-1]:
            print(Y[N//2])
        else:
            print(Y[N//2-1])


if __name__ == '__main__':
    main()