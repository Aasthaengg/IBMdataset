import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = [int(input()) for _ in range(N)]
from collections import Counter

c = Counter(As)
ans = 0
for i, cnt in c.most_common():
    if cnt%2==0:
        continue
    else:
        ans += 1

print(ans)