from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]


print((b-1 + a - 2)//(a-1))