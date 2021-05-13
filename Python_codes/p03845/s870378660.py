import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
T = list(map(int, input().split()))
M = int(input())
sum_  = sum(T)
for _ in range(M):
    P, X = map(int, input().split())
    ans = sum_ - T[P-1] + X
    print(ans)