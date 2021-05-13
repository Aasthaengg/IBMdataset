import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
A = list(map(int, input().split()))
A.sort()

start = 0
end = (3 * N) - 1

ans = 0
while True:
    end -= 1
    ans += A[end]
    start += 1
    end -= 1
    if start > end:
        break

print(ans)
