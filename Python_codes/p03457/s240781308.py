N = int(input())
P = []

for _ in range(N):
    t, x, y = input().split()
    p = [int(t), int(x), int(y)]
    P.append(p)

t_before = 0
x_before = 0
y_before = 0
f_enable = True
for p in P:
    t, x, y = p

    t_distance = abs(t_before - t)
    p_distance = abs(x_before - x) + abs(y_before - y)

    distance = t_distance - p_distance

    if distance < 0:
        f_enable = False
        break
    elif distance % 2 != 0:
        f_enable = False
        break

    t_before = t
    x_before = x
    y_before = y

if f_enable:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)