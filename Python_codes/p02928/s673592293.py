N,K = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i] > A[j]:
            cnt += 1

cnt2 = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            cnt2 += 1

ans = (cnt*K + cnt2*(K*(K-1)//2))%(10**9 + 7)
print(ans)