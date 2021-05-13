S = int(input())
v = 10**9

y = S//v + (S < 10**18)
x = v*y - S

print(0, 0, 10**9, 1, x, y)