n, m =  map(int, input().split())

ac = (n - m) * 100
tle = m * 1900

print((ac + tle)* 2**m)