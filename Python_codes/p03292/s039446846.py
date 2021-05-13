from sys import stdin

A, B, C = [int(x) for x in stdin.readline().rstrip().split()]

print(max(A,B,C)-min(A,B,C))