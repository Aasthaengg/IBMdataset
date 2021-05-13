from sys import stdin
import bisect

x,a,b = [int(x) for x in stdin.readline().rstrip().split()]

if abs(x-a) > abs(x-b):
    print("B")
else:
    print("A")