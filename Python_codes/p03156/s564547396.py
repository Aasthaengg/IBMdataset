from sys import stdin
N = int(stdin.readline().rstrip())
A, B = [int(_) for _ in stdin.readline().rstrip().split()]
P = [int(_) for _ in stdin.readline().rstrip().split()]
a, ab, b = 0, 0, 0
for p in P:
    if p <= A:
        a += 1
    elif A < p <= B:
        ab += 1
    elif B < p:
        b += 1
print(min(a, ab, b))