s = int(input())

v = 10**9
x = (v - s % v) % v
y = (s + x) // (10**9)

print('0 0 1000000000 1', x, y)
