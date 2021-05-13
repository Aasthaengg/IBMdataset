n,m = map(int,input().split())
a = [input().split() for i in range(n)]
b = [input().split() for i in range(m)]

for i in range(n):
    distance = 10000000000
    for j in range(m):
        temp = abs(int(a[i][0]) - int(b[j][0])) + abs(int(a[i][1]) - int(b[j][1]))
        if distance > temp:
            ans = j + 1
        distance = min(temp,distance)
    print(ans)