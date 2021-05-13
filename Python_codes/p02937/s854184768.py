# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from bisect import bisect_left
from collections import defaultdict
import sys
def main(S, T):
    D = defaultdict(list)
    for i, s in enumerate(S):
        D[s].append(i + 1)
    cycle = 0
    idx = 0
    N = len(S)
    for t in T:
        if not D[t]:
            return -1
        i = bisect_left(D[t], idx + 1)
        if i >= len(D[t]):
            cycle += 1
            idx = D[t][0]
        else:
            idx = D[t][i]
    return cycle * N + idx

if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    t = input().rstrip()
    ans = main(s, t)
    print(ans)
