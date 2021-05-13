import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    S = input()
    L = len(S)
    d = defaultdict(list)

    i = 0
    for s in S:
        d[s].append(i)
        i += 1

    ans = INF

    for indexs in d.values():
        last = -1
        result = 0
        for i in indexs:
            tmp = i - last - 1
            result = max(result, tmp)
            last = i
        result = max(result,L-last-1)
        ans = min(ans, result)

    if ans == 0:
        ans = '0 '
        print(ans)
    else:
        print(ans)


if __name__ == '__main__':
    main()
