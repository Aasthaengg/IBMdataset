from sys import stdin

n = int(stdin.readline())

a = [int(x) for x in stdin.readline().split(' ')]
b = a[:n]
b.reverse()

print(' '.join([str(i) for i in b]))