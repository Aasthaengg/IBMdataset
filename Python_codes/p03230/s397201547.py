import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import itertools

N = int(input())
k = 1
while k * (k+1) // 2 <= N:
    k += 1

if k * (k-1) // 2 == N:
    S = [[] for _ in range(k)]
    for i,(a,b) in enumerate(itertools.combinations(range(k),2),1):
        S[a].append(i)
        S[b].append(i)
    print('Yes')
    print(k)
    for se in S:
        print(len(se), *se)
else:
    print('No')