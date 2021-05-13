N = int(input())
A = [int(n) for n in input().split()]
flg = 1
cnt = 0
while flg:
    flg = 0
    for i in range(N-1, 0, -1):
        if A[i] < A[i-1]:
            t = A[i]
            A[i] = A[i-1]
            A[i-1] = t
            flg = 1
            cnt += 1
for i in range(N):
    if i == N - 1:
        print(A[i])
    else:
        print(A[i], end=" ")
print(cnt)