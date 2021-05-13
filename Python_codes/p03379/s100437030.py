def main():
    N = int(input())
    X = list(map(int, input().split()))
    sorted_X = sorted(X)
    overall_med = (sorted_X[N//2 - 1] + sorted_X[N//2]) // 2
    for x in X:
        if x <= overall_med:
            print(sorted_X[N//2])
        else:
            print(sorted_X[N//2 - 1])


if __name__ == '__main__':
    main()
