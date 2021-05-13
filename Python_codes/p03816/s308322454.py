from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
s = len(set(A))
if s % 2 != 0:
    print(s)
else:
    print(s-1)