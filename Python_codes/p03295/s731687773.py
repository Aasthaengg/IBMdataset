n, m = map(int, input().split())
lis = []
for i in range(m):
    a, b = map(int, input().split())
    lis.append((a, b))

lis.sort(key=lambda x:x[1])

res = [lis[0]]
for i in range(1, m):
    if res[-1][0] < lis[i][1] and lis[i][0] < res[-1][1]:
        continue
    else:
        res.append((lis[i][0], lis[i][1]))
print(len(res))