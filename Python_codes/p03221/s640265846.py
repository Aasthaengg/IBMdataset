n, m = map(int, input().split())
city = []
for i in range(m):
    p, y = map(int, input().split())
    city.append([p, y, i])

city.sort(key=lambda x:x[1])
city.sort()

res = [''] * m
cnt = 1
for i in range(m):
    res[city[i][2]] = str(city[i][0]).zfill(6) + str(cnt).zfill(6)
    if i + 1 < m and city[i][0] == city[i+1][0]:
        cnt += 1
    else:
        cnt = 1


for num in res:
    print(num)