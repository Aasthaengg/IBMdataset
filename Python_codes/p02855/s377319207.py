import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
from itertools import accumulate #list(accumulate(A))

H, W, K = mi()
S = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
l = [0] * H
for i in range(H):
    l[i] = sum([S[i][j] == '#' for j in range(W)])

l = list(accumulate(l))
#print(l)

ans = dp2(0, W, H)
num = 1
for i in range(H):
    if (i==l[i]==0):
        continue
    elif (i>0 and l[i]==l[i-1]):
        for j in range(W):
            ans[i][j] = ans[i-1][j]
    else:
        for j in range(W):
            ans[i][j] = min(num, l[i])
            if S[i][j] == '#':
                num += 1

for i in reversed(range(H)):
    if ans[i][0] == 0:
        for j in range(W):
            ans[i][j] = ans[i+1][j]

#print(ans)
for i in range(H):
    for j in range(W):
        print(ans[i][j], end='')
        if j != W-1:
            print(' ', end='')
    print('')