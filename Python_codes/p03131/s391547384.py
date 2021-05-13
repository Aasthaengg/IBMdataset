#temprate
from sys import setrecursionlimit
setrecursionlimit(10**6)
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#temprate
K,A,B = inputlist()
if A >= B:
    print(K + 1)
    exit()

tmp = K - (A - 1)
if tmp < 0:
    print(K + 1)
    exit()
cnt = tmp // 2
amari = tmp % 2

ans = cnt * B - (cnt - 1) * A + amari
ans = max(ans, K + 1)
print(ans)