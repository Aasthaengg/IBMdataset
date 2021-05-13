N = int(input())
A = list(map(int, input().split()))
cnt = 0
chge = 0
for i in range(N):
    mn = A[i]
    for j in range(i+1, N):
        if mn > A[j]:
            mn = A[j]
            idx = j
            chge = 1
    if chge:
        A[idx] = A[i]
        A[i] = mn
        cnt += 1
        chge = 0

for i in range(N):
    if i == N - 1:
        print(A[i])
    else:
        print(str(A[i]), end = " ")
print(cnt)