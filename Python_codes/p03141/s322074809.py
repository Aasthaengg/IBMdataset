import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ab = [list(map(int, readline().split())) for i in range(n)]
memo = [0] * n
ans = 0
for i, ab_ in enumerate(ab):
    memo[i] = ab_[0] + ab_[1]
    ans -= ab_[1]
memo.sort(reverse=True)
for i in range(n):
    if i % 2 == 0:
        ans += memo[i]
print(ans)
