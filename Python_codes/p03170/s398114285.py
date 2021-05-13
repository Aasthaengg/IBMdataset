# https://kyopro-friends.hatenablog.com/entry/2019/01/12/231000

def main():
    import sys
    readline = sys.stdin.readline

    n, k = map(int, readline().rstrip().split())
    *a, = sorted(map(int, readline().split()))

    dp = [False] * (k + 1)
    dp[0] = False
    # dp[手番開始時の石の個数]:=勝敗

    for i in range(1, k + 1):
        for x in a:
            if x > i: break
            if not dp[i - x]:
                dp[i] = True
                break

    print('First' if dp[k] else 'Second')


if __name__ == '__main__':
    main()
