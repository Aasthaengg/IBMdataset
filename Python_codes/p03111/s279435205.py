import sys

N,A,B,C = map(int,sys.stdin.readline().rstrip().split())
l = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

from itertools import product

# 各々の竹をAに使うか、Bに使うか、Cに使うか、使わないかで全探索

ans = 10**18
for a in list(product([1,2,3,4],repeat=N)):
    X,Y,Z = [],[],[]
    for i in range(N):
        if a[i] == 1:
            X.append(l[i])
        elif a[i] == 2:
            Y.append(l[i])
        elif a[i] == 3:
            Z.append(l[i])
    if len(X) == 0 or len(Y) == 0 or len(Z) == 0:
        continue
    else:
        a = 0
        a += 10*(len(X)+len(Y)+len(Z)-3)
        a += abs(A-sum(X)) + abs(B-sum(Y)) + abs(C-sum(Z))
        if a < ans:
            ans = a

print(ans)
