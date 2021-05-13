from sys import stdin
A, V = [int(_) for _ in stdin.readline().rstrip().split()]
B, W = [int(_) for _ in stdin.readline().rstrip().split()]
T = int(stdin.readline().rstrip())
if abs(A-B) <= (V-W)*T:
    print("YES")
else:
    print("NO")