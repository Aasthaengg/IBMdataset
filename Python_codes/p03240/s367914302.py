N = int(input())

infos = []
first_info = []
for _ in range(N):
    x, y, h = map(int, input().split())
    if h > 0 and len(first_info) == 0:
        first_info = [x, y, h]
    else:
        infos.append([x, y, h])


# cxとcyを1つに絞り込む
x1, y1, h1 = first_info
for cx in range(101):
    for cy in range(101):
        isValid = True
        H = h1 + abs(x1-cx) + abs(y1-cy)
        for x2, y2, h2 in infos:
            if h2 != max(H - abs(x2-cx) - abs(y2-cy), 0):
                isValid = False

        if isValid:
            ans = [cx, cy]

cx, cy = ans
H = h1 + abs(x1-cx) + abs(y1-cy)
print(cx, cy, H)
