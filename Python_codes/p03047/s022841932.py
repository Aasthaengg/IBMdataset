from sys import stdin

N = [int(x) for x in stdin.readline().rstrip().split()]

print(N[0] - N[1] + 1)