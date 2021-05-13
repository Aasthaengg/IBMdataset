from sys import stdin

n, a, b = [int(x) for x in stdin.readline().rstrip().split()]

print(min(n*a, b))