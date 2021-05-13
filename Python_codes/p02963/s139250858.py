# https://atcoder.jp/contests/agc036/tasks/agc036_a

S = int(input())
x1 = 0
y1 = 0
x2 = 1000000000
y2 = 1
v = 1000000000
x = (v - S % v) % v
y = (S + x) // v

print("{} {} {} {} {} {}".format(x1, y1, x2, y2, x, y))