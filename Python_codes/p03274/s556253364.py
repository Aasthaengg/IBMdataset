def main():
    n,k = map(int,input().split())
    X = list(map(int,input().split()))

    ans = 10**9

    for i in range(n-k+1):
        t1 = abs(X[i]) + abs(X[i] - X[i+k-1])
        t2 = abs(X[i+k-1]) + abs(X[i] - X[i+k-1])
        t = min(t1,t2)

        ans = min(ans,t)

    print(ans)



main()