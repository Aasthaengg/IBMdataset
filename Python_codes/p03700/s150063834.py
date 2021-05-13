N,A,B = map(int,input().split())
h = [0]*N
for i in range(N):
    h[i] = int(input())

# x回で全モンスター倒せるかどうかをにぶちゃん(にぱー)

import math

def check(x):
    count = 0
    for i in range(N):
        count += math.ceil(max(h[i] - B * x, 0) / (A - B))
           
    if count <= x:
        return True
    else:
        return False
    
def solve():
    
    left = -1
    right = 10**9+1
    
    while abs(right-left) > 1:
    
        center = (right+left)//2
    
        if check(center) == True:
            right = center
        elif check(center) == False:
            left = center
        
    return right
    
print(solve())