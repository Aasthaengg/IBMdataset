def near(x, Y):
    i = bisect_left(Y,x)
    if i == 0:
        return Y[i]-x
    elif i == len(Y):
        return x-Y[i-1]
    else:
        return min(Y[i]-x, x-Y[i-1])

def near2(x, Y):
    i = bisect_left(Y,x)
    if i == 0:
        return Y[i]-x + D[i][1]
    elif i == len(Y):
        return x-Y[i-1] + D[i-1][1]
    else:
        return min(Y[i]-x+D[i][1], x-Y[i-1]+D[i-1][1])

from bisect import *
A, B, Q = map(int, input().split())
S = []
T = []
for _ in range(A):
    S.append(int(input()))
for _ in range(B):
    T.append(int(input()))
D = []
for a in S:
    D.append((a, near(a, T)))
for b in T:
    D.append((b, near(b, S)))
D.sort(key=lambda x:x[0])
D2 = [d for d, _ in D]
for _ in range(Q):
    x = int(input())
    print(near2(x,D2))

