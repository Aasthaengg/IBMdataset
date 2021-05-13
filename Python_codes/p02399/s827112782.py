from sys import stdin

a, b = (int(n) for n in stdin.readline().rstrip().split())

d, r, f = (a // b, a % b, a / b)

print("{} {} {:.6f}".format(d, r, f))
