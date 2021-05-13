def score():
    A,B,C,K = list(map(int,input().split()))

    if K<A+B:
        if K<A:
            print(K)
            return
        print(A)
        return
    print(A-(K-A-B))
    return

score()
