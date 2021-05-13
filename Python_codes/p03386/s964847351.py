A, B, K = map(int, input().split())
for i in range(A, A + K):
    if i > B:
        break
    print(i)
for j in range(B - K + 1, B + 1):
    if j < A or j <= i:
        continue
    print(j)
