import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
ab = [tuple(map(int, input().split())) for _ in range(m)]
from heapq import heappop as hpp, heappush as hp
h = []
for i,(a,b) in enumerate(ab):
    hp(h, (a,i,0))
ans = 0
m = -1
while h:
    val,ind,c = hpp(h)
    if c==0:
        hp(h, (ab[ind][1],ind,1))
    else:
        if m>=0 and ab[ind][0]<=m<val:
            pass
        else:
            m = ab[ind][1]-1
            ans += 1
#             print(val,ind,c)
print(ans)