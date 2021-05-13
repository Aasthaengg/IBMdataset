import sys,math,collections,itertools
input = sys.stdin.readline

N,K=list(map(int,input().split()))
A = list(map(int,input().split()))

for i in range(K):
    imo = [0]*(N+1)
    flag = 1
    for j in range(N):
        imo[max(0,j-A[j])] += 1
        imo[min(N,j+A[j]+1)] -= 1
        if j-A[j]>0 or j+A[j]+1<N:
            flag = 0
    A = list(itertools.accumulate(imo))[:-1]
    if flag == 1:
        break
print(*A)
