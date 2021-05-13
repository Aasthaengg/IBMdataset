def main():
    N = int(input())
    X = [int(a) for a in input().split()]
    Xs = sorted(X)

    for i in range(len(X)):
        if  Xs[len(Xs)//2] > X[i]:
            print(Xs[len(Xs)//2])
        else:
            print(Xs[len(Xs)//2 - 1])

if __name__ == "__main__":
    main()