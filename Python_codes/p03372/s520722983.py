import sys
input = sys.stdin.buffer.readline

n, c = map(int, input().split())
X = [0]*n
V = [0]*n
for i in range(n):
    x, v = map(int, input().split())
    X[i] = x
    V[i] = v

from itertools import accumulate
# clock
A1 = [0]+V
A1 = list(accumulate(A1))
for i, x in enumerate(X):
    A1[i+1] -= x
#print(A1)

# counterclock
B1 = [0]+list(reversed(V))
B1 = list(accumulate(B1))
for i, x in enumerate(reversed(X)):
    B1[i+1] -= c-x
#print(B1)

import copy
MA1 = copy.copy(A1)
for i in range(1, n+1):
    MA1[i] = max(MA1[i-1], A1[i])

MB1 = copy.copy(B1)
for i in range(1, n+1):
    MB1[i] = max(MB1[i-1], B1[i])

#print(MA1)
#print(MB1)

A2 = copy.copy(A1)
for i, x in enumerate(X):
    A2[i+1] -= x
#print(A2)

B2 = copy.copy(B1)
for i, x in enumerate(reversed(X)):
    B2[i+1] -= c-x
#print(B2)

MA2 = copy.copy(A2)
for i in range(1, n+1):
    MA2[i] = max(MA2[i-1], A2[i])

MB2 = copy.copy(B2)
for i in range(1, n+1):
    MB2[i] = max(MB2[i-1], B2[i])

#print(MA2)
#print(MB2)

ans = 0
# clock > counterclock
for i in range(n+1):
    temp = MA2[i]+MB1[n-i]
    ans = max(ans, temp)
# counterclock > clock
for i in range(n+1):
    temp = MB2[i]+MA1[n-i]
    ans = max(ans, temp)
print(ans)
