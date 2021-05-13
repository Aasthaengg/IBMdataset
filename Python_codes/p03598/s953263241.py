def resolve():
    N = int(input())
    K = int(input())
    ans = 0
    X = list(map(int,input().split()))
    for i in range(N): 
        if X[i] > K - X[i] :
            ans = ans + K - X[i]
        else:
            ans = ans + X[i]
    print(ans*2)
resolve()