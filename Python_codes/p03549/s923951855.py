n, m = map(int, input().split())

time_once = 100*(n-m) + 1900*m
r = 2**m

x = r*time_once

print(x)
