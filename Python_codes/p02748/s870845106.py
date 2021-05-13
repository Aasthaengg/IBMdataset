A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for _ in range(M)]
# print(xyc)
cost = []
cost.append(min(a) + min(b))
for x, y, c in xyc:
    tmp = a[x - 1] + b[y - 1] - c
    cost.append(tmp)
print(min(cost))
