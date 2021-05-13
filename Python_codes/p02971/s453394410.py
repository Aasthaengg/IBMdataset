import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
A = [I() for _ in range(N)]

B = [0]*N
C = [0]*N
for i in range(N):
    if i == 0:
        B[i] = A[i]
    else:
        B[i] = max(B[i-1],A[i])
for i in range(N-1,-1,-1):
    if i == N-1:
        C[i] = A[-1]
    else:
        C[i] = max(C[i+1],A[i])

for i in range(N):
    if i == 0:
        print(C[1])
    elif i == N-1:
        print(B[-2])
    else:
        print(max(B[i-1],C[i+1]))
