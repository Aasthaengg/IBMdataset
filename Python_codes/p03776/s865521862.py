def comb(N):
    for i in range(N+1):
        for j in range(i+1):
            if j == 0 or j == i :
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

def main():
    global dp,N
    N, A, B = map(int, input().split())
    v = [int(i) for i in input().split()]
    v.sort(reverse=True)
    dp = [[0 for i in range(N+1)] for j in range(N+1)]
    ans = 0
    for i in range(A):
        ans += v[i]
    ans /= A
    a = 0
    b = 0
    for i in range(N):
        if v[A-1] == v[i]:
            a += 1
            if i < A :
                b += 1
    ans_2 = 0
    comb(N)
    if v[A-1] == v[0]:
        for i in range(A,B+1):
            ans_2 += dp[a][i]
    else:
        ans_2 += dp[a][b]
    print(ans,ans_2)


if __name__ == '__main__':
    main()
