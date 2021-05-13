n, h, w = map(int, input().split())
alloy = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in alloy:
    a, b = i[0], i[1]
    if a >= h and b >= w:
        res += 1

print(res)
