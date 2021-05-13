import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ds = [int(input()) for _ in range(N)]
print(len(set(Ds)))