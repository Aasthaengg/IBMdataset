def main():
    N = int(input())
    dp = [0] * N
    rt = int(pow(N, 0.5)) + 1
    for i in range(1, rt):
        ii = i * i
        for j in range(1, i + 1):
            iji = ii + j * j + i * j
            if iji + 1 + i + j > N:
                break
            for k in range(1, j + 1):
                c = iji + k * k + (i + j) * k
                if c <= N:
                    if i == j or j == k:
                        l = 3
                        if i == k:
                            l = 1
                    else:
                        l = 6
                    dp[c - 1] += l
                else:
                    break
    print("\n".join(map(str,dp)))


if __name__ == "__main__":
    main()
