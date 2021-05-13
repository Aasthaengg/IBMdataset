import sys

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
A = list(map(int, input().split()))


ans = INF
for a in A:
    cnt = 0
    while True:
        q, mod = divmod(a, 2)
        if mod != 0:
            break
        cnt += 1
        a = q
    ans = min(ans, cnt)
print(ans)
