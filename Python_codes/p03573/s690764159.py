from sys import stdin
A,B,C = [int(x) for x in stdin.readline().rstrip().split()]
d = sorted([A,B,C])
if d[0] == d[1]:
    print(d[2])
else:
    print(d[0])