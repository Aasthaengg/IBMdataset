def route_num(stairs):
    if stairs <= 1:
        return 1
    else:
        return route_num(stairs - 1) + route_num(stairs - 2)

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

broken = {i:False for i in range(n + 1)}
for a_i in a:
    broken[a_i] = True

route_num = {}
for i in range(n + 1):
    if broken[i]:
        route_num[i] = 0
    elif i <= 1:
        route_num[i] = 1
    else:
        route_num[i] = (route_num[i-1] + route_num[i-2]) % 1000000007

print(route_num[n])
