import sys
input=sys.stdin.readline
def main():
    N, K = map(int, input().split())
    lst_a = list(map(int, input().split()))
    # 石の個数が残りi個の局面で勝ちTrue 負け False　
    dp = [False] * (K+1)
    for i in range(1, K+1):
        for j in range(N):
            if i - lst_a[j] >= 0:
                dp[i] |= not(dp[i - lst_a[j]])
    
    if dp[K]:
        print('First')
    else:
        print('Second')
main()