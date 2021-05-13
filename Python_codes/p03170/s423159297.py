import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    dp = [False] * (K+1)

    for i in range(0,K+1):
        for a in A:
            if i - a >= 0:
                # 遷移先に一つでもFalseがあれば遷移元dp[i]を勝ち(True)にできる
                # 遷移先が全てTrueであれば、勝つことはできないので遷移元dp[i]はFalseになる
                dp[i] = dp[i] or (not dp[i-a])

    if dp[K]:
        print('First')
    else:
        print('Second')




if __name__ == '__main__':
    main()
