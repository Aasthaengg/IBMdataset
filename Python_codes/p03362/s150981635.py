import math
from collections import deque

N = int(input())

def prime(n):
    if(n == 1):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
        
    return True
A = []
cnt = 0
for i in range(2, 55556):
    if(prime(i)):
        if(i % 5 == 1):
            A.append(i)
            cnt += 1
            if(cnt == N):
                break
                
for i in range(N):
    print(A[i], end=' ')