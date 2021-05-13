import sys
readline = sys.stdin.readline

A,B,K = map(int,readline().split())

print(max(A - K, 0),max(B - (max(K - A, 0)),0))