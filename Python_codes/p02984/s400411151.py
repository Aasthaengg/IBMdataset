N = int(input())
A = list(map(int,input().split()))

B = [0] * N
for i,a in enumerate(A):
    if i < N- 1:
        B[i+1] = A[i] * 2 - B[i]
    else:
        diff = A[i] - (B[i] + B[0])//2

B = [diff]
for i,a in enumerate(A):
    if i < N-1:
        B.append(A[i]*2 - B[i])

print(*B)