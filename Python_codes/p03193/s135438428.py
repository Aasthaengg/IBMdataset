n, h, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    hight = ab[i][0] // h
    width = ab[i][1] // w
    if hight >= 1 and width >= 1:
        count += min(hight, width)

print(count)