A, B, K = map(int, input().split())

k = K-1
if A+k >= B-k:
    for i in range(A, B+1):
        print(i)
else:
    for j in range(A, A+k+1):
        print(j)
    for k in range(B-k, B+1):
        print(k)
