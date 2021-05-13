n = int(input())

r = []
c = 1
i = 1
while i <= n:
    r.append([])
    for j in range(1, c+1):
        r[-1].append(i)
        i += 1
    c += 1

if i == n+1:
    print('Yes')
    print(c)
    for j in range(c-1):
        result = [c-1]
        result.extend(r[j])
        for x in range(j+1, c-1):
            result.append(r[x][j])
        print(*result)
    result = [c-1]
    for x in range(c-1):
        result.append(r[x][x])
    print(*result)
else:
    print("No")
