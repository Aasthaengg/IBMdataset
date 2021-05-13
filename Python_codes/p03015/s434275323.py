import sys
sys.setrecursionlimit(1000000)
MOD = 10**9 + 7

def main():
    l = input()
    dp1 = 0
    dp2 = 1
    for i in range(len(l)):
        dp1 = 3 * dp1
        if l[i] == '0':
            dp2 = dp2
        else:
            dp1 += dp2
            dp2 = 2 * dp2
        dp1 %= MOD
        dp2 %= MOD
    print((dp1 + dp2) % MOD)

main()