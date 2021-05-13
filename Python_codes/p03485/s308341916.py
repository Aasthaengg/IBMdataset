from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]

print(int((a+b)/2 + 0.9))