"""
N = list(map(int,input().split()))
S = [str(input()) for _ in range(N)]
S = [list(map(int,list(input()))) for _ in range(h)] 
print(*S,sep="")
"""

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

a,b = map(int,input().split())

if (a*b)%2==0:
    print("Even")
else:
    print("Odd")