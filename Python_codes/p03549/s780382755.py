import sys
input = sys.stdin.readline
n,m=map(int,input().split())
print(((n-m)*100+1900*m)*2**m)
