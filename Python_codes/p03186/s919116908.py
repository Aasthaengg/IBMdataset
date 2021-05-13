from sys import stdin
A, B, C = [int(_) for _ in stdin.readline().rstrip().split()]
if A+B+1 >= C:
    print(B+C)
else:
    print(B*2+A+1)
