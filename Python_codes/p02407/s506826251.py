from sys import stdin

stdin.readline()

a_n = list(stdin.readline().rstrip().split())
a_n.reverse()

print(" ".join(a_n))
