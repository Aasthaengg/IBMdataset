n = int(input())
c = input()

lw, rr = [0]*(n+1), [c.count('R')]*(n+1)
for i in range(n):
    lw[i+1] = lw[i] + (c[i] == 'W')
    rr[i+1] = rr[i] - (c[i] == 'R')


def operation(left_white, right_red):
    swap = min(left_white, right_red)
    white_to_red, red_to_white = max(0, left_white-swap), max(0, right_red-swap)
    return swap + white_to_red + red_to_white


print(min(operation(white, red) for white, red in zip(lw, rr)))
