import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def combinations_count(n, r):
    if n == 1:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    S = SI()
    
    ls = []
    len_S = len(S)
    rem = 0

    for s in range(len_S-1,-1,-1):
        rem = (rem+int(S[s])* pow(10, len_S-s-1, 2019))%2019
        ls.append(rem)
    
    import collections

    cls = collections.Counter(ls)
    clsv= list(cls.values())

    ans = 0

    for p in clsv:
        ans += combinations_count(p,2)
    ans += cls[0]
    print(ans)



if __name__ == '__main__':
    main()