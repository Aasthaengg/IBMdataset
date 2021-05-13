import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    money = [1]
    for i in range(10):
        money.append(money[-1]*6)
    money.append(9)
    for i in range(9):
        money.append(money[-1]*9)
    
    dp = [INF] * (1 + N)
    dp[0] = 0
    for m in money:
        for j in range(m,N + 1):
            dp[j] = min(dp[j],dp[j - m] + 1)
    ans = dp[-1]
    print(ans)
if __name__ == '__main__':
    main()