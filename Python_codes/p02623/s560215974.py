# 再帰は深くなりすぎる
N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
accum_A, accum_B = [0] * (len(A)+1), [0] * (len(B)+1)
for i in range(len(A)):
    accum_A[i+1] = accum_A[i] + A[i]
for i in range(len(B)):
    accum_B[i+1] = accum_B[i] + B[i]

ans = 0
i, j = len(A), 0
while i >= 0 and j <= len(B) :
    if accum_A[i] + accum_B[j] > K:
        i -= 1
    else:
        ans = max(ans, i+j)
        j += 1

print(ans)
