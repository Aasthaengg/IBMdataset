from sys import stdin
N, A, B = [int(_) for _ in stdin.readline().rstrip().split()]
print(min(A, B), max(0, A+B-N))