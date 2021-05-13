import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, C, K = mapint()

Ts = [int(input()) for _ in range(N)]
Ts.sort()
last_cus = Ts[0]
cum = 1
bus = 0
for i in range(1, N):
    t = Ts[i]
    last_cus = min(last_cus, t)
    if t-last_cus>K:
        bus += 1
        cum = 0
        last_cus = t
    cum += 1
    if cum==C:
        bus += 1
        cum = 0
        last_cus = 10**18
if cum!=0:
    print(bus+1)
else:
    print(bus)