X, Y = map(int, input().split())
ans = 10 ** 18

# flipしない
if Y - X >= 0:
    ans = Y - X

# はじめにflip
if Y - (-X) >= 0:
    ans = min(ans, 1 + Y - (-X))

# 最後にflip
if (-Y) - X >= 0:
    ans = min(ans, (-Y) - X + 1)

# 両方flip
if (-Y) - (-X) >= 0:
    ans = min(ans, 1 + (-Y) - (-X) + 1)

print(ans)
