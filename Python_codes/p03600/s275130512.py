import math,itertools,bisect,sys,copy,queue
INF = 10**20

def LI(): return [int(x) for x in sys.stdin.readline().split()]

N = int(input())
A = [LI() for _ in range(N)]
a = copy.deepcopy(A)


for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0 or A[i][k] == 0 or A[k][j] == 0: continue
            if A[i][j] > A[i][k] + A[k][j]:
                print (-1)
                exit (0)
            if A[i][j] == A[i][k] + A[k][j]:
                A[i][j] = 0
print (sum(sum(A[i]) for i in range(N) )//2)