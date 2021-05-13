import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ab = [0] * m
for i in range(m):
    aa, bb = map(int, input().split())
    ab[i] = (aa, bb)

ab.sort()
ans = 1
prev_left, border = ab[0][0], ab[0][1]
for i in range(1, m):
    if prev_left == ab[i][0]:
        border = min(border, ab[i][1])
    else:
        if border <= ab[i][0]:
            ans += 1
            border = ab[i][1]
        prev_left = ab[i][0]
        border = min(border, ab[i][1])
print(ans)