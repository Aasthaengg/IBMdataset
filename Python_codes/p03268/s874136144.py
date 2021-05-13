import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N, K = mi()
    
cnt_n = 0
ini_n = K
while ini_n <= N:
    cnt_n += 1
    ini_n += K

ans = cnt_n ** 3

if K % 2 == 0:
    ini_k = K // 2
    cnt_k = 0
    while ini_k <= N:
        cnt_k += 1
        ini_k += K
    ans += cnt_k ** 3

print(ans)