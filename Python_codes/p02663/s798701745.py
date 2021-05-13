from sys import stdin
H1, M1, H2, M2, K = [int(_) for _ in stdin.readline().rstrip().split()]
print(((H2-H1)*60 + (M2-M1)) - K)