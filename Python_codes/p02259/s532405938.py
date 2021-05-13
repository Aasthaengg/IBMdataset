N = int(input())
A = list(map(int, input().split()))
n = N
cnt = 0
while n > 0:
    for i in range(N-1, 0, -1):
        if A[i] < A[i-1]:
            t = A[i]
            A[i] = A[i-1]
            A[i-1] = t
            cnt += 1
    n -= 1
for i in range(N):
    if i == N - 1:
        print(str(A[i]))
    else:
        print(str(A[i]) + " ", end = "")
print(cnt)