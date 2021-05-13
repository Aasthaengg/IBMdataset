n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
list = [list(map(int, input().split())) for x in range(m)]
list.sort(key=lambda x: x[1], reverse=True) # １番の要素で降順ソート

app_count = 0
for i in list:
    a += [i[1]]*i[0]
    app_count += i[0]
    if app_count>n:
        break

a.sort(reverse=True)

print(sum(a[:n]))
