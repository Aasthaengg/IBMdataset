# coding: utf-8

N, A, B, C = int(input()), input(), input(), input()
cnt = 0
for i in range(N):
    if A[i] == B[i] and A[i] == C[i]:
       pass
    elif (A[i] == B[i] and A[i] != C[i]) or (A[i] == C[i] and A[i] != B[i]) or (B[i] == C[i] and A[i] != B[i]):
        cnt += 1
    else:
        cnt += 2
print(cnt)