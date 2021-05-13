n, c, k = map(int, input().split())
t = []
for _ in range(n):
    t.append(int(input()))
t.sort()
passenger = 0
bus_flag = False
bus_launch = 0
ans = 0
for i in range(n):
    if not bus_flag:
        bus_launch = t[i] + k
        bus_flag = True

    if t[i] <= bus_launch:
        passenger += 1
        if passenger == c:
            ans += 1
            bus_flag = False
            passenger = 0
    else:
        ans += 1
        bus_launch = t[i] + k
        passenger = 1

if passenger != 0:
    ans += 1
print(ans)


