from sys import stdin
N, K = [int(_) for _ in stdin.readline().rstrip().split()]
print(N-K+1)