X, Y = map(int, input().split())
n = 0
t_leg = 2
k_leg = 4

for i in range(101):
    for s in range(101):
        if X - i - s == 0 and Y - 2 * i - 4 * s == 0:
            n += 1

if n > 0:
    print("Yes")
else:
    print("No")