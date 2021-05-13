import sys
input = sys.stdin.readline

A,B,T=list(map(int,input().split()))
print(B*(T//A))
