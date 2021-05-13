import math
import sys
MOD = 1000000007

h, w, k = map(int, input().split())

if w == 1:
    print(1)
    sys.exit()

A = [[1]]


def bit(x, i):
    return (x >> i) & 1


def invalid(x):
    ans = False
    for j in range(w):
        if bit(x, j) == 1 and bit(x, j+1) == 1:
            ans = True
    return ans


for i in range(w-1):
    A[0].append(0)

for i in range(1, h+1):
    A.append([])
    for j in range(w):
        A[i].append(0)
    for x in range(2**(w-1)):
        if(invalid(x)):
            continue
        
        # corner case
        if bit(x, 0) == 1:
            A[i][0] = (A[i][0] + A[i-1][1]) % MOD
        else:
            A[i][0] = (A[i][0] + A[i-1][0]) % MOD
        if bit(x, w-2) == 1:
            A[i][w-1] = (A[i][w-1] + A[i-1][w-2]) % MOD
        else:
            A[i][w-1] = (A[i][w-1] + A[i-1][w-1]) % MOD
        
        for j in range(1, w-1):
            if bit(x, j-1) == 1:
                A[i][j] = (A[i][j] + A[i-1][j-1]) % MOD
            elif bit(x, j) == 1:
                A[i][j] = (A[i][j] + A[i-1][j+1]) % MOD
            else:
                A[i][j] = (A[i][j] + A[i-1][j]) % MOD

#print(A)

print(A[h][k-1])
