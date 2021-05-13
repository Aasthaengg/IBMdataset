import math

def eratosthenes(limit):
    A = [i for i in range(2, limit+1)]
    P = []
    pt = []
    time = 0
    
    while True:
        prime = min(A)
        
        if prime > math.sqrt(limit):
            break
            
        P.append(prime)
            
        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
            
    for a in A:
        P.append(a)

    for p in P:
        if p%5 ==1:
            pt.append(p)
     
    return pt

limit = 55555
P = eratosthenes(limit)

n = int(input())
print(*P[:n])
