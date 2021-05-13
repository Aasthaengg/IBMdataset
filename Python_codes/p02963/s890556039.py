# https://atcoder.jp/contests/agc036/tasks/agc036_a

s = int(input())

x1, y1 = 0, 0
x2 = 10 ** 9
y2 = 1

y3 = (s + x2 -1) // x2
x3 = x2 * y3 - s
print(x1, y1, x2, y2, x3, y3)