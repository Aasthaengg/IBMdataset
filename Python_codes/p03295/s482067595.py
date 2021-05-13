import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
 
N, M = mi()
Q = li2(M)
Q = sorted(Q, key=lambda x:x[1])
 
#table = dp2(0, N, N)
 
#for i in range(M):
    #s, t = mi()
    #for i in range(t):
    #table[s-1][t-1] = 1
 
#for i in reversed(range(N-1)):
    #for j in range(i, N):
        #table[i][j] = max(table[i+1][j], table[i][j])
 
#print(table)
'''
i = j = 0
cnt = 0
while True:
    while j < N and table[i][j] == 0:
        j += 1
    if j >= N:
        break
    cnt += 1
    i = j
 
print(cnt)
'''
 
l = [N]*N
for i in range(M):
    ind = max(0, Q[i][0]-1)
    l[ind] = min(Q[i][1]-1, l[ind])
 
for i in reversed(range(N-1)):
    l[i] = min(l[i], l[i+1])
 
cnt = 0
i = 0
#print(l)
while True:
    i = l[i]
    cnt += 1
    if l[i] == N:
        break
 
print(cnt)