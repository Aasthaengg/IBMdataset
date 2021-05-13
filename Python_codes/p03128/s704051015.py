import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    dp = [(0, 0)] * (N + 1) # dp[i] = (i本のマッチで作れる最大の整数, その整数の桁数)
    for n in range(N + 1):
        for a in A:
            if n - Match[a] < 0: continue
            if n - Match[a] == 0:
                dp[n] = max(dp[n], (a, 1))
                continue
            number, l = dp[n - Match[a]]
            if number != 0: dp[n] = max(dp[n], (number + a * 10**l, l + 1))
    print(dp[N][0])

if __name__ == "__main__":
    main()
