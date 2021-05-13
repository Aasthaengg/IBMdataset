from sys import stdin
N,A,B = [int(x) for x in stdin.readline().rstrip().split()]
MAX = min(A,B)
MIN = max(A+B-N,0)
print(MAX,MIN)