def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    X = [0] * N
    cur = sum(A) - 2 * sum(A[1::2])
    X[0] = cur
    for i, a in enumerate(A[:-1], 1):
        X[i] = a * 2 - cur
        cur = X[i]
    print(' '.join(map(str, X)))
    


if __name__ == "__main__":
    main()
