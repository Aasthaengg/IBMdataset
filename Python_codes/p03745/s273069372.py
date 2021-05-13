n = int(input())
*a, = map(int, input().split())
ans = 1
up = False
down = False
prev = a.pop(0)
for i in a:
    if (not up) and (not down):
        if prev < i:
            up = True
        elif prev > i:
            down = True
    elif up:
        if prev > i:
            ans += 1
            up = False
    elif down:
        if prev < i:
            ans += 1
            down = False
    prev = i
print(ans)