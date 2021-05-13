from sys import stdin
from itertools import accumulate

a,b,c = [int(x) for x in stdin.readline().rstrip().split()]

if a<= c <= b:
    print("Yes")
else:
    print("No")
