from sys import stdin
from itertools import repeat
def main():
    n = int(stdin.readline())
    dp = [1] * (n + 1)
    a = map(int, stdin, repeat(10, n))
    d = {}
    for i, x in enumerate(a):
        dp[i+1] = dp[i]
        if x in d and d[x] < i:
            dp[i+1] += dp[d[x]]
            if dp[i+1] >= 1000000007:
                dp[i+1] -= 1000000007
        d[x] = i + 1
    print dp[-1]
main()
