from collections import defaultdict

def main():
    """
    n = argmax(dp)とすると、
    (n - dp[n], n]は操作を行わなくてok

    逆にそれ以外の数は1回操作する
    -> N - dp[n]
    """
    N = int(input())

    dp = defaultdict(int)

    for _ in range(N):
        p = int(input())
        dp[p] = dp[p - 1] + 1
    
    print(N - max(dp.values()))

if __name__ == "__main__":
    main()