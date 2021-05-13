n, m = map(int, input().split())
l = []

for i in range(m):
    p, y = input().split()
    l.append([p, int(y), i])

l.sort()

l[0][1] = 1

for i in range(1, m):
    if l[i][0] == l[i - 1][0]:
        l[i][1] = l[i - 1][1] + 1
    else:
        l[i][1] = 1

sortthird = lambda val: val[2]
l.sort(key = sortthird)

for i in l:
    ans = "0"*(6 - len(i[0])) + i[0] + "0"*(6 - len(str(i[1]))) + str(i[1])
    print(ans)