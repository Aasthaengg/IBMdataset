n, x = map(int, input().split())
list = list(map(int, input().split()))

jump_point = [0]
tmp = 0
for point in list:
    tmp += point
    jump_point.append(tmp)

ans = 0
for i in jump_point:
    if i <= x:
        ans += 1

print(ans)