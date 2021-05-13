import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N, K, = map(int, input().split())

print(0 if N % K == 0 else 1)