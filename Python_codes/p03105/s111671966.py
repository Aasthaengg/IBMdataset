import sys
sys.setrecursionlimit(10**6)

a,b,c=map(int,input().split())

print(min(b//a,c))
