from math import ceil
n, h = map(int, input().split())
data1, data2 = [], []
for i in range(n):
    a, b = map(int, input().split())
    data1.append([a, b])
    data2.append([a, b])

data1 = sorted(data1, key = lambda x: x[0], reverse = True)
data2 = sorted(data2, key = lambda x: x[1], reverse = True)
ans = 0
while h > 0 and data1[0][0] < data2[0][1]:
    h -= data2[0][1]
    ans += 1
    del data2[0]
    if len(data2) == 0:
        break
ans += ceil(max(0, h) / data1[0][0])
print(ans)