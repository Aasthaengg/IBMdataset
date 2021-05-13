# ABC052D - Walk and Teleport (ARC067D)
def main():
    N, A, B = tuple(map(int, input().split()))
    X = tuple(map(int, input().split()))
    D = [j - i for i, j in zip(X, X[1:])]  # distance
    ans = sum(min(A * d, B) for d in D)
    print(ans)


if __name__ == "__main__":
    main()