import sys
input = sys.stdin.readline

A,B,C = sorted(list(map(int,input().split())))
print('Yes' if A+B == C else 'No')