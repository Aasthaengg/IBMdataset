import sys
input = sys.stdin.readline
N,A,B = [int(i) for i in input().split()]
print(min(N * A , B))