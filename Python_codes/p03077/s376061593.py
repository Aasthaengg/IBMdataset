import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
ABCDE = [int(input()) for _ in range(5)]
MIN = min(ABCDE)

print(-(-N//MIN)+4)