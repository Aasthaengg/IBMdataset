import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
K = int(input())
Xs = list(mapint())

ans = 0
for x in Xs:
    ans += min(abs(x), abs(x-K))*2
print(ans)