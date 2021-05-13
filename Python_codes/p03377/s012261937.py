from sys import stdin
A, B, C = [int(x) for x in stdin.readline().rstrip().split()]
if C<=(A+B) and A <= C:
    print("YES")
else:
    print("NO")