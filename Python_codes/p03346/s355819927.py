def main():
    N,*P=map(int, open(0).read().split())
    X=[0]*(N+1)
    for p in P:
        X[p]=max(X[p],X[p-1]+1)
    print(N-max(X))

if __name__ == "__main__":
    main()