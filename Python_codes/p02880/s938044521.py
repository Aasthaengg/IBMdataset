import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
s = set()
for i in range(1, 10):
    for j in range(1, 10):
        s.add(i*j)
if N in s:
    print('Yes')
else:
    print('No')