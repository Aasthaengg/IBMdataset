A, B, C, K = map(int, input().split())
mai = min(A, K)
acc = mai
if mai < K:
    mai += B
if mai < K:
    acc -= K - mai
print(acc)
