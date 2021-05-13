from sys import stdin
A,B = [int(x) for x in stdin.readline().rstrip().split()]
a1 = A + B
a2 = A - B
a3 = A * B

print(max(a1,a2,a3))