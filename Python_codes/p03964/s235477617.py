n = int(input())
x, y = 1, 1
for _ in range(n):
    t, a = map(int, input().split())
    if x <= t and y <= a:
        x = t
        y = a
    else:
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