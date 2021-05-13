import sys
input = sys.stdin.readline

A,B=list(map(int,input().split()))
print(max(A+(A-1),B+(B-1),A+B))
