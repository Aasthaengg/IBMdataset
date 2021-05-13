import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())
a = list(map(int,readline().split()))

if sum(a) == 0:
    print('Yes')
    exit()

if N%3 != 0:
    print('No')
    exit()

from collections import Counter

ac = Counter(a).most_common()

if len(ac) == 3 and ac[0][1] == ac[1][1] == ac[2][1] and ac[0][0] ^ ac[1][0] == ac[2][0]:
    print('Yes')

elif len(ac) == 2 and ac[0][1] == ac[1][1]*2 and ac[0][0] ^ ac[0][0] == ac[1][0]:
    print('Yes')
else:
    print('No')
