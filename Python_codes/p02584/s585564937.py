x, k, d = map(int, input().split())
if (x - k*d > 0 and x > 0) or (x + k*d < 0 and x < 0):
    print(abs(x) - k*d )
else:
    if x % d == 0:
        if ((x/d) % 2) == (k % 2):
            print(0)
        else:
            print(d)
    else:
        y = abs(x)
        if (y % d < d - (y % d) and ((y - (y % d)) / d) % 2 == k % 2) or (y % d > d - (y % d) and ((y - (y % d)) / d) % 2 == k % 2):
            print(y % d)
        else:
            print(d - (y % d))