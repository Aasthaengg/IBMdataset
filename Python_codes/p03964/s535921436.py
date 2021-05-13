n = int(input())
x, y = 1, 1
for _ in range(n):
    t, a = map(int, input().split())
    if x <= t and y <= a:
        x = t
        y = a
    elif x <= t and y > a:
        if y % a == 0:
            i = y // a
        else:
            i = y // a + 1
        y = i*a
        x = i*t
    elif x > t and y <= a:
        if x % t == 0:
            i = x // t
        else:
            i = x // t + 1
        x = i*t
        y = i*a
    elif x > t and y > a:
        if x % t == 0:
            i_x = x // t
        else:
            i_x = x // t + 1

        if y % a == 0:
            i_y = y // a
        else:
            i_y = y // a + 1
        bigger = max(i_x, i_y)
        x = bigger*t
        y = bigger*a
print(x+y)