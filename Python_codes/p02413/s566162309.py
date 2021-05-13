r, c = map(int, input().split())
li = []
last_r =[0 for _ in range(c + 1)]
for i in range(r):
    li.append([int(x) for x in input().split()])
    li[i].append(sum(li[i]))
    for j in range(c+1):
        last_r[j] +=li[i][j]
li.append(last_r)
for i in li:
    print(*i)