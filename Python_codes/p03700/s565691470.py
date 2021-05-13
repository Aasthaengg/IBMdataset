# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, A, B = map(int, readline().split())
H = list(map(int,read().split()))
H = sorted(H,reverse = True)
t = A-B

def solve(x):
    cnt = 0
    for i in range(N):
        rem = H[i]-x*B
        if rem <= 0:
            break
        else:
            cnt += -(-rem // t)
    if cnt <= x:
        return True
    else:
        return False 
    

left = 0
right = 10**9
while right - left > 1:
    x = (left + right) // 2
    flag = solve(x)
    if flag:
        right = x
    else:
        left = x
        
print(right)