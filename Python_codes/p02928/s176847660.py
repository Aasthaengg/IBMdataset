p = 10**9+7
N,K = map(int,input().split())
A = list(map(int,input().split()))
cnt_in = 0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i]>A[j]:
            cnt_in += 1
A = A+A
cnt_out=0
for i in range(2*N-1):
    for j in range(i+1,2*N):
        if A[i]>A[j]:
            cnt_out += 1
cnt_out = cnt_out-2*cnt_in
cnt = K*cnt_in
cnt = (cnt+cnt_out*(K*(K-1))//2)%p
print(cnt)