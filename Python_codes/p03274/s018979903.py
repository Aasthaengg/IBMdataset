def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    ans = float('inf')
    for i in range(N-K+1):
        L = x[i]
        R = x[i+K-1]
        if R < 0:
            ans = min(ans, abs(L))
        elif L <= 0 <= R:
            ans = min(2*abs(R)+abs(L), 2*abs(L)+abs(R), ans)
        elif 0 < L:
            ans = min(ans, abs(R))
        else:
            continue
    
    print(ans)

if __name__ == "__main__":
    main()
