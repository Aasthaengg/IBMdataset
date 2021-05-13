import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

W, a, b = mapint()
if a>b:
    a, b = b, a
print(max(0, b-(a+W)))