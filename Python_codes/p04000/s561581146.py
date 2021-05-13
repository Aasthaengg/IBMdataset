import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

H, W, N = map(int, input().split())
cand = set()
dot = set()
for _ in range(N):
    x, y = map(int, input().split())
    dot.add((x, y))
    for i in range(-2, 1):
        if 1 <= x + i <= H - 2:
            for j in range(-2, 1):
                if 1 <= y + j <= W - 2:
                    cand.add((x + i, y + j))

ans = [0] * 10
for x, y in cand:
    cnt = 0
    for i in range(3):
        for j in range(3):
            cnt += int((x + i, y + j) in dot)
    ans[cnt] += 1

zero = (H - 2) * (W - 2) - sum(ans)
ans[0] = zero
print(*ans, sep="\n")