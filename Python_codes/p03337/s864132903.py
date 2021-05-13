from sys import stdin
import bisect

a,b = [int(x) for x in stdin.readline().rstrip().split()]

print(max(a+b,a-b,a*b))