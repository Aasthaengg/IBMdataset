# -*- coding: utf-8 -*-
from collections import deque

H,W = list(map(int, input().rstrip().split()))
A_list = [list(input().rstrip()) for i in range(H)]
#-----

def check(matrix):
    for i in range(len(matrix)):
        matrix[i] = ["#"] + matrix[i][:] + ["#"]
    
    matrix = [["#"]*(W+2)] + matrix[:] + [["#"]*(W+2)]
    
    
    # queue = [ (row, column) ]
    # deque = [ (int, int   ) ]
    queue = deque()
    
    for i in range(1,H+1):
        for j in range(1, W+1):
            if matrix[i][j] == "#":
                queue.append( (i, j) )
    
    
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    step = -1
    
    while queue:
        step += 1
        
        for _ in range(len(queue)):
            r,c = queue.popleft()
            
            for d in delta:
                next_r = r + d[0]
                next_c = c + d[1]
                
                if matrix[next_r][next_c] == ".":
                    matrix[next_r][next_c] = "#"
                    queue.append( (next_r, next_c) )


    return step

#-----

ans = check(A_list)
print(ans)
