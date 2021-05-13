import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
B = list(map(int, input().split()))

A = [INF] * N
for i in range(N-1):
    A[i] = min(A[i], B[i])
    A[i+1] = min(A[i+1], B[i])
    # print(A)
ans = sum(A)
print(ans)