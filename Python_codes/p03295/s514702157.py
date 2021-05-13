N, M = map(int, input().split())
islands = [tuple(map(int, input().split())) for _ in range(M)]
islands.sort()

cnt = 0
l = 1
r = N
for left, right in islands:
    if r <= left:
        cnt += 1
        l = left
        r = right
    else:
        l = max(l, left)
        r = min(r, right)

print(cnt+1)