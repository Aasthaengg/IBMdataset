import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())

dishes = [a, b, c, d, e]

min_m = 10
for dish in dishes:
    diff = dish % 10
    if diff > 0:
        min_m = min(min_m, diff)

ans = 0
tmp = -1
for dish in dishes:
    diff = dish % 10
    if min_m != 10 and diff == min_m and tmp == -1:
        tmp = dish
    else:
        if diff:
            ans += dish + 10 - diff
        else:
            ans += dish
tmp = 0 if tmp == -1 else tmp
print(ans + tmp)