import sys,math
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float('inf')
MOD = 10**9+7
dy = [0,1,0,-1]
dx = [1,0,-1,0]
ddy = [0,1,1,1,0,-1,-1,-1]
ddx = [1,1,0,-1,-1,-1,0,1]

n,k = map(int,input().split())
if math.ceil(n/2) >= k:
    print('YES')
else:
    print('NO')