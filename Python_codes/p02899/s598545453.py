import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

lis = [-1]*N
for i in range(N):
    a = As[i]
    lis[a-1] = str(i+1)
print(' '.join(lis))
