n, c, k = map(int, input().split())
t = sorted(int(input()) for _ in range(n))
cnt = 0
bus_people = 0
bus_time = 0
for i in range(n):
    if bus_people >= c or t[i] > bus_time:
        bus_people = 1
        bus_time = t[i] + k
        cnt += 1
    else:
        bus_people += 1
print(cnt)