import sys,math,collections,itertools
input = sys.stdin.readline
m = 10**9+7
N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
Aaf = []
Aall = []
for i in range(N):
    cntall= 0
    cntaf = 0
    for j in range(N):
        if A[i]>A[j]:
            cntall +=1
            if i < j :
                cntaf += 1
    Aaf.append(cntaf)
    Aall.append(cntall)

cnt=0
for a0,a1 in zip(Aaf,Aall):
    cnt += (K*a0+a1*K*(K-1)//2)%m
print(cnt%m)
