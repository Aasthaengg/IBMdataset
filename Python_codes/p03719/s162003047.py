import sys
input = sys.stdin.readline

A,B,C=list(map(int,input().split()))
print('Yes' if A<=C<=B else 'No')