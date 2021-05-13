import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, T = map(int, input().split())
time = list(map(int, input().split()))

ans = T
for x, y in zip(time[:-1], time[1:]):
    ans += min(T, y - x)
print(ans)