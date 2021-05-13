import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
from heapq import heappop as hpp, heappush as hp
h = []
for num in a:
    hp(h, -num)
for _ in range(m):
    val = hpp(h)
    val *= -1
    hp(h, -(val//2))
ans = -sum(h)
print(ans)