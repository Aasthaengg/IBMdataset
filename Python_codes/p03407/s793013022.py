import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())
print('Yes' if A+B >= C else 'No')