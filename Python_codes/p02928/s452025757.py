p = 10**9+7
N,K = map(int,input().split())
A = list(map(int,input().split()))
inner=0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i]>A[j]:
            inner += 1
B = A+A
outer = 0
for i in range(2*N-1):
    for j in range(i+1,2*N):
        if B[i]>B[j]:
            outer += 1
outer -= 2*inner
cnt = (inner*K)%p
a = ((K*(K-1))//2)%p
cnt = (cnt+outer*a)%p
print(cnt)