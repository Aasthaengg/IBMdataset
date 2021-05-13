import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
n = int(input())
v = list(map(int, input().split()))
from heapq import heappop as hpp, heappush as hp
h = []
for num in v:
    hp(h, num)
while len(h)>=2:
    v0, v1 = hpp(h), hpp(h)
    hp(h, (v0+v1)/2)
ans = h[0]
print(ans)