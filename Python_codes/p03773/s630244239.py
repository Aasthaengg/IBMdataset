from sys import stdin
inp = lambda : stdin.readline().strip()

a, b = [int(x) for x in inp().split()]
print((a+b)%24)