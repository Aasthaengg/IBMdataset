n = int(input())
a = []
a.append([int(i) for i in input().split()])
a.append([int(i) for i in input().split()])
ans = 0
for i in range(n):
    tmp = a[0][0]
    x = 0
    y = 0
    for j in range(n):
        if i == j:
            y += 1
        else:
            x += 1
        tmp += a[y][x]
    ans = max(tmp,ans)
print(ans)
