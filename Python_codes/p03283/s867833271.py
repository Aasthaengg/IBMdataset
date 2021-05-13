import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

N,M,Q = map(int,S().split())
A = [[0]*(N+2) for _ in range(N+2)]
# A[i][j] = [i,j]に完全に含まれる列車の本数

for i in range(M):
    L,R = LI()
    A[0][R] += 1
    A[L+1][R] -= 1

from itertools import accumulate

# 二重累積和

for i in range(N+2):
    A[i] = list(accumulate(A[i]))

for i in range(N+2):
    for j in range(N+2):
        if i == 0 or j == 0:
            continue
        else:
            A[i][j] += A[i-1][j]

for i in range(Q):
    p,q = LI()
    print(A[p][q])