def main():

    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
    v = 0
    for i in range(N-1):
        v += min((X[i+1] - X[i]) * A, B)
    return v

if __name__ == '__main__':
    print(main())