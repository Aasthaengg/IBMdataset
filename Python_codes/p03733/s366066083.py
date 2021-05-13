def main():
    N,T = map(int,input().split())
    t = list(map(int,input().split()))
    ans = 0

    dp = [0] * N
    dp[0] = t[0]
    for i, tt in enumerate(t):
        if i == N-1:
            ans += T
            break
        if tt + T > t[i+1]:
            ans += t[i+1] - tt
        else:
            ans += T
    print(ans)

if __name__ == '__main__':
    main()
