sentinel = 10 ** 9 + 10 ** 8

X, Y, A, B, C = map(int, input().split())
ps = [sentinel] + sorted(map(int, input().split()), reverse = True)
qs = [sentinel] + sorted(map(int, input().split()), reverse = True)
rs = sorted(map(int, input().split()), reverse = True)

X += 1
Y += 1

red_apples = X
green_apples = Y

while X+Y-red_apples-green_apples < C:
    if rs[X+Y-red_apples-green_apples] > qs[green_apples-1]:
        if qs[green_apples-1] > ps[red_apples-1]:
            red_apples -= 1
        else:
            green_apples -= 1
    elif rs[X+Y-red_apples-green_apples] > ps[red_apples-1]:
            red_apples -= 1
    else:
        break

print(sum(ps[1:red_apples]) + sum(qs[1:green_apples]) + sum(rs[:X+Y-red_apples-green_apples]))
