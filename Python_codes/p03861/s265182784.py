"""
N = list(map(int,input().split()))
S = [str(input()) for _ in range(N)]
S = [list(map(int,list(input()))) for _ in range(h)] 
print(*S,sep="")
"""

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

a,b,x = map(int,input().split())

first = x*(a//x + bool(a%x))
end = x*(b//x)
if first==end:
    print(1)
elif first>end:
    print(0)
else:
    print((end-first)//x+1)
