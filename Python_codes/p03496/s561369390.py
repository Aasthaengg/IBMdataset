N = int(input())
A = list(map(int, input().split()))

M, Mi = 0, 0
for i, a in enumerate(A):
    if abs(a) > abs(M):
        M = a
        Mi = i

ans = []
if M > 0:
    for i in range(N):
        ans.append((Mi, i))
        A[i] += A[Mi]

    for i in range(N - 1):
        if A[i] > A[i + 1]:
            ans.append((i, i + 1))
            A[i + 1] += A[i]

else:
    for i in range(N):
        ans.append((Mi, i))
        A[i] += A[Mi]
    
    for i in range(N - 1, 0, -1):
        if A[i - 1] > A[i]:
            ans.append((i, i - 1))
            A[i - 1] += A[i]

print(len(ans))
for x, y in ans:
    print(x + 1, y + 1)
