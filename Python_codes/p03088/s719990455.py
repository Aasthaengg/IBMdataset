# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from itertools import product
from collections import defaultdict
import sys
MOD = 10**9 + 7
def main(N):
    dp = [defaultdict(int) for _ in range(N + 1)]
    dp[0]['TTT'] = 1
    for i in range(N):
        for j in product('AGCT', repeat=3):
            jj = ''.join(j)
            if jj not in dp[i]: continue
            for k in 'AGCT':
                last4 = jj + k
                last3 = last4[1:]
                if last3 == 'AGC': continue
                if last3 == 'GAC': continue
                if last3 == 'ACG': continue
                if last4[0] == 'A' and last4[3] == 'C' and (last4[1] == 'G' or last4[2] == 'G'): continue
                dp[i + 1][last3] += dp[i][jj]
                dp[i + 1][last3] %= MOD
    ans = 0
    for j in product('AGCT', repeat=3):
        jj = ''.join(j)
        ans += dp[N][jj]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    main(N)
