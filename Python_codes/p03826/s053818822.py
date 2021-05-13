from sys import stdin

a,b,c,d = [int(x) for x in stdin.readline().rstrip().split()]

print(max(a*b,c*d))