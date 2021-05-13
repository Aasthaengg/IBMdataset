import sys

readline = sys.stdin.readline

def main():
    n, m = map(int, readline().split())
    c = list(map(int, readline().split()))

    maxnum = 50001
    DP = [maxnum] * (n+1)
    DP[0] = 0
    for ctmp in c:
        for j in range(ctmp, n+1):
            if DP[j-ctmp] == maxnum:
                continue
            else:
                DP[j] = min(DP[j], DP[j-ctmp] + 1)
    
    ans = DP[n]
    print(ans)


if __name__ == "__main__":
    main()

