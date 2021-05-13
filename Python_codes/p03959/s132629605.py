N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
mami = []
ans = 1
mod = 10**9 + 7
for i in range(N):
    mi, ma = 1 , min(T[i], A[i])+1
    if i != N-1:
        if A[i] > A[i+1]:
            mi = A[i]
    else :
        mi = A[i]
    if i != 0 :
        if T[i] > T[i-1]:
            mi = T[i]
    else :
        mi = T[i]            
    ans = (max(ma - mi, 0) * ans ) % mod
print (ans)
