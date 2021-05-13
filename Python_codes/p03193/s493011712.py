n, h, w = map(int, input().split())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
cnt = 0
for j in ab:
    if j[0] >= h and j[1] >= w:
        cnt += 1
print(cnt)