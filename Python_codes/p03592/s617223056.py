import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, K = mapint()

s = set()
for n in range(N+1):
    for m in range(M+1):
        s.add(n*M + m*N - n*m*2)

if K in s:
    print('Yes')
else:
    print('No')