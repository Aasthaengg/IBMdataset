n, m = map(int, input().split())

time_f = 100 * (n - m) * (2**m)
time_l = 1900 * (2**m) * m

print(time_l + time_f)