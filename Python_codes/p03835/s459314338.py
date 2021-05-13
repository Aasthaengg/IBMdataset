K,S = map(int,input().split())
x = y = S//3
z = S - x - y
if z < y:
    x = z
    z = y
ans = 0
while 0 <= x <= y and 0<= y <=K and z <= K:
    while 0 <= x and z <= K:
        if x == y == z:
            ans += 1
        elif x == y or y == z:
            ans += 3
        else:
            ans += 6
        x -= 1
        z += 1
    y -= 1
    x = y
    z = S - x - y
    if z < y:
        x = z
        z = y
x = y = S//3 + 1
z = S - x - y
if z < y:
    x = z
    z = y
while 0 <= x <= y and 0 <= y <= K and y <= z <= K:
    while 0 <= x and z <= K:
        if x == y == z:
            ans += 1
        elif x == y or y == z:
            ans += 3
        else:
            ans += 6
        x -= 1
        z += 1
    y += 1
    x = y
    z = S - x - y
    if z < y:
        x = z
        z = y
print(ans)