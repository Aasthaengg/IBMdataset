import sys
input = sys.stdin.readline

"""
def dfs(x, y):
    if x==0 and y==0:
        return False
        
    res = False
    
    if x>0:
        res |= not dfs(x-1, y)
    
    if y>0:
        res |= not dfs(x, y-1)
    
    if min(x, y)>0:
        res |= not dfs(x-1, y-1)
    
    return res
    
t = [[False]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        t[i][j] = dfs(i, j)

for ti in t:
    print(*ti)
"""

N = int(input())
a = [int(input()) for _ in range(N)]

for ai in a:
    if ai%2==1:
        print('first')
        exit()

print('second')