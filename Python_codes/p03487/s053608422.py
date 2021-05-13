import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
from collections import Counter
c = Counter(As)

ans = 0
for num, c in c.most_common():
    if c>num:
        ans += c-num
    elif c<num:
        ans += c

print(ans)