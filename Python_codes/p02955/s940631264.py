N,K = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
ans = 1
C = []
for i in range(1,int(S**0.5+1)):
    if S%i == 0:
        C.append(i)
        C.append(S//i)
for c in C:
    B = []
    for i in A:
        B.append(i%c)
    B.sort()
    hoge = 0
    sum_b = sum(B)
    for i in range(N):
        hoge += B[i]
        sum_b -= B[i]
        if hoge <= K and hoge == c*(N-i-1)-sum_b:
            ans = max(ans,c)
print(ans)