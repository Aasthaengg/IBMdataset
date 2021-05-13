x, y = map(int, input().split())

ans = int(1e11)

# B(0) --> A --> B(0)
if x <= y:
    ans = min(ans, y - x)

# B(1) --> A --> B(0)
if -x <= y:
    ans = min(ans, y + x + 1)

# B(0) --> A --> B(1)
if x <= -y:
    ans = min(ans, -y - x + 1)

# B(1) --> A --> B(1)
if -x <= -y:
    ans = min(ans, -y + x + 2)

print(ans)