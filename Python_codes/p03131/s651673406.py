k, a, b = map(int, input().split())
bis = 1
if b - a <= 2:
    bis += k
else:
    while k != 0:
        if bis >= a and k >= 2:
            bis += b - a
            k -= 2
        else:
            bis += 1
            k -= 1
print(bis)