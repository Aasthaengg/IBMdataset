from bisect import bisect_right
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
F = [0 for _ in range(N+1)]
for i in range(N-1,-1,-1):
    b = B[i]
    indC = bisect_right(C,b)
    if i<N-1:
        indC1 = bisect_right(C,B[i+1])
    else:
        indC1 = N
    F[i] = F[i+1]+indC1-indC
G = [0 for _ in range(N+1)]
for i in range(N-1,-1,-1):
    G[i] = G[i+1]+F[i]
cnt = 0
for i in range(N):
    a = A[i]
    indB = bisect_right(B,a)
    cnt += G[indB]
print(cnt)