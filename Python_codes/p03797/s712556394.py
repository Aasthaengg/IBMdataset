import sys
input = sys.stdin.readline
n,m=map(int,input().split())
print(min(m//2,(n+m//2)//2))
