from sys import stdin

a = sorted([int(x) for x in stdin.readline().rstrip().split()])
print(abs(a[0] - a[1]) + abs(a[1] - a[2]))
