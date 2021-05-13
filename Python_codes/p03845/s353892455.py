import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
T = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    P, X = map(int, input().split())
    ans = 0
    for i in range(N):
        if i + 1 == P:
            ans += X
        else:
            ans += T[i]
    print(ans)