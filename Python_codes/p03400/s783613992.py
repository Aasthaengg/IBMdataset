def resolve():
    N = int(input())
    D, X = map(int,input().split())
    for i in range(N):
        Ai = int(input())
        X += (D-1) // Ai + 1
    print(X)
resolve()