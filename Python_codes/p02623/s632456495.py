N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = [0]
B = [0]
for i in range(len(a)):
    A.append(A[i] + a[i])
for i in range(len(b)):
    B.append(B[i] + b[i])

ans = 0
j = len(B) - 1
for i in range(len(A)):
    if A[i] > K:
        break
    while A[i] + B[j] > K:
        j -= 1
    ans = max(ans, i + j)
print(ans)
