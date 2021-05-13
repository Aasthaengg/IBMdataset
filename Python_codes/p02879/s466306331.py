import sys
input = sys.stdin.readline

A,B = list(input().rstrip().split())
print( -1 if len(A) >1 or len(B) > 1 else eval(A+'*'+B))
