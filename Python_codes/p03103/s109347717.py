n, m = map(int, input().split())
list = []
for i in range(n) :
    a, b = map(int, input().split())
    list.append([a, b])
list.sort(key=lambda x:x[0])
count = 0 ; ans = 0
for i in range(n) :
    if list[i][1] < m - count :
        ans += list[i][0] * list[i][1]
        count += list[i][1]
    elif list[i][1] >= m - count :
        ans += list[i][0] * (m - count)
        break
print(ans)
