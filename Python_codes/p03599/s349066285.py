def main():
    A, B, C, D, E, F = list(map(int, input().split()))
    A *= 100
    B *= 100
    dp = [[0] * 3000 for _ in range(3000)]
    dp[0][0] = 1
    m = 0
    mt = (A, 0)
    for i in range(3000):
        for j in range(3000):
            if dp[i][j] == 0:
                continue
            if i + A <= F:
                dp[i+A][j] = 1
            if i + B <= F:
                dp[i+B][j] = 1
            if i + C <= F:
                dp[i+C][j+C] = 1
                if (j+C)/(i+C) > m and (j+C)/(i+C)<= E/(100+E):
                    m = (j+C)/(i+C)
                    mt = ((i+C), (j+C))
            if i + D <= F:
                dp[i+D][j+D] = 1
                if (j+D)/(i+D) > m and (j+D)/(i+D)<= E/(100+E):
                    m = (j+D)/(i+D)
                    mt = ((i+D), (j+D))
    return mt
mt = main()
print(mt[0], mt[1])

