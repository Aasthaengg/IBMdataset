p = 10**9+7
N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
H = [0 for _ in range(N)]
cnt = 1
H[0] = T[0]
for i in range(1,N):
    if T[i]>T[i-1]:
        H[i] = T[i]
if H[-1]>0 and H[-1]!=A[-1]:
    cnt = 0
else:
    H[-1] = A[-1]
    for i in range(-2,-N-1,-1):
        if H[i]==0 and A[i]>A[i+1]:
            if A[i]<=T[i]:
                H[i] = A[i]
            else:
                cnt = 0
                break
        elif H[i]>0 and A[i]>A[i+1]:
            if H[i]==A[i]:continue
            else:
                cnt = 0
                break
    if cnt==1:
        for i in range(1,N-1):
            if H[i]==0:
                cnt = (cnt*min(T[i],A[i]))%p
print(cnt) 