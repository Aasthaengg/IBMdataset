n = int(input())
data = []

for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])
data = sorted(data, key = lambda x: x[1])
time = 0
ans = "Yes"
for i in range(n):
    if time + data[i][0] > data[i][1]:
        ans = "No"
    time += data[i][0]
print(ans)