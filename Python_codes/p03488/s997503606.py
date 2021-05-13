# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from itertools import groupby
import sys
def main(s, x, y):
    g = [x, y]
    o = [[], []]

    direction = count = 0
    first = True
    for c in s:
        if c == 'T':
            if first:
                g[0] -= count
                first = False
            elif count > 0:
                o[direction].append(count)
            count = 0
            direction ^= 1
        else:
            count += 1
    if first:
        g[0] -= count
    elif count > 0:
        o[direction].append(count)

    for d in range(2):
        l = o[d]
        M = sum(l)
        M2 = M * 2
        if abs(g[d]) > M:
            print('No')
            return
        pre = [False] * (M2 + 1)
        pre[M] = True
        for i, v in enumerate(l):
            dp = [False] * (M2 + 1)
            for a in range(M2 + 1):
                if pre[a] == False: continue
                if a >= v:
                    dp[a - v] = True
                if a + v <= M2:
                    dp[a + v] = True
            pre = dp
        if pre[g[d] + M] == False:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    x, y = map(int, input().split())
    main(s, x, y)
