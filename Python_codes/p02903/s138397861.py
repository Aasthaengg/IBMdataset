import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main(): 
    h,w,a,b = map(int,input().split())
    grid = [['0']*w for _ in range(h)]

    if a == 0:
        for i in range(b):
            grid[i] = ['1'] * w

    elif b == 0:
        for i in range(h):
            for j in range(a):
                grid[i][j] = '1'
                
    else:
        for i in range(b):
            for j in range(a):
                grid[i][j] = '1'
            for j in range(2*a,w):
                grid[i][j] = '1'
        
        for i in range(b,2*b):
            for j in range(a,2*a):
                grid[i][j] = '1'
        
        for i in range(2*b,h):
            for j in range(a):
                grid[i][j] = '1'
    
    for i in range(h):
        print(''.join(grid[i]))  
    
if __name__=='__main__':
    main()
