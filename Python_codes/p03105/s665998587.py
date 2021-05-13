import sys
input = sys.stdin.readline

A,B,C=list(map(int,input().split()))
print(min(B//A,C))
