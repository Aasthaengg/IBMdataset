# -*- coding: utf-8 -*-
# C - Base -2 Number
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def positive_solve(n):
    for i in range(1,30):
        if (4**i-1) // 3 >= n:
            tmp = i
            break
    return 2*tmp-2
    
def negative_solve(n):
    for i in range(1,30):
        if (4**i-1)*2 // 3 >= n:
            tmp = i
            break
    return 2*tmp-1

N = int(readline())
A = []
while True:
    if N == 0:
        break
    if N > 0:
        bit = positive_solve(N)
        A.append(bit)
        N -= 2**bit
    else:
        bit = negative_solve(-N)
        A.append(bit)
        N += 2**bit
        
S = len(A)
if S == 0:
    print(0)
else:
    A = sorted(A)
    p = 0
    ans = ''
    for i in range(A[-1]+1):
        if i == A[p]:
            ans += '1'
            p += 1
        else:
            ans += '0'
    print(ans[::-1])