#AGC014-B Unplanned Queries
"""
今回は各辺の偶奇のみを考えるので、
根付き木を考えた時に、頂点a,bから親側に全部流した時に、
LCAより先は勝手に偶数になるので無視できる。
とした場合に、根をrootとして、各クエリに対して
a-root,b-rootへのパスに1を足すことと考えると、
結局各辺の偶奇はaとbの出現回数の偶奇によると考える事ができる。
よって、クエリに与えられる辺の回数をdictで保持し、
最終的に一つでも奇数回出現する頂点があるならばFalse
そうでないならTrueとなる

"""
import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m = map(int,readline().split())
dic1 = defaultdict(int)
for i in range(m):
    a,b = map(int,readline().split())
    dic1[a] += 1
    dic1[b] += 1

for i in dic1.values():
    if not even(i):
        print("NO")
        exit()
print("YES")