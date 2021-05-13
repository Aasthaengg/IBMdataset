n, x, t = map(int, input().split())
if n % x == 0 :
    time_lapse = (int(n / x)) * t
    print(time_lapse)
else:
    time_lapse = (int(n / x) + 1) * t
    print(time_lapse)