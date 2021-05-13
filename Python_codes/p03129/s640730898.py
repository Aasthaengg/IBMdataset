from sys import stdin
N, K = [int(_) for _ in stdin.readline().rstrip().split()]
if N >= K*2-1:
    print("YES")
else:
    print("NO")