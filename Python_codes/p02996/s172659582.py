n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort(key = lambda x : x[1])
now = 0
for i in range(n):
    now += data[i][0]
    if now > data[i][1]:
        print("No")
        exit()
print("Yes")