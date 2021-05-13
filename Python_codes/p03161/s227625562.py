def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    INF = 10**10
    DP = [INF]*N
    DP[0] = 0
    DP[1] = abs(h[1]-h[0])
    for i in range(2,N):
        DP[i] = min(DP[i-j] + abs(h[i-j]-h[i]) for j in range(1,min(K,i)+1))
    print(DP[-1])
    
if __name__ == "__main__":
    main()
