def main():
    H,N = [int(x) for x in input().split()]
    A,B = [],[]
    for _ in range(N):
        a,b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)

    dp = [float('inf')]*(H+1)
    dp[0] = 0
    for i in range(N):
        for j in range(H+1):
            # print(i,j,dp[j],A[i],B[i])
            dp[min(j+A[i],H)] = min(dp[min(j+A[i],H)], dp[j]+B[i])
            # print(dp)
    print(int(dp[H]))


if __name__ == '__main__':
    main()