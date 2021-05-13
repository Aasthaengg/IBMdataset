def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    DP = [10**10 for _ in range(N)]
    DP[0] = 0
    DP[1] = abs(h[0]-h[1])
    
    for i in range(2, N):
        DP[i] = min(DP[k]+abs(h[i]-h[k]) for k in range(max(0, i-K), i))    
    print(DP[N-1])
main()