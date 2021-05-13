# ABC052D - Walk and Teleport (ARC067D)
def main():
    # choose A * dist(i, j) or B greedily
    N, A, B, *X = map(int, open(0).read().split())
    ans = sum(min(A * (j - i), B) for i, j in zip(X, X[1:]))
    print(ans)


if __name__ == "__main__":
    main()