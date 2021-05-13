import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
s = set()
for _ in range(N):
    s.add(int(input()))

lis = list(s)
lis.sort()
print(len(lis))