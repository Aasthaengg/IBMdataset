K, T = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
# print('A', A)

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == 0:
            break
        v = min(A[i], A[j])
        A[i] -= v
        A[j] -= v

cnt = 0
for i in range(len(A)):
    if A[i] >= 1:
        cnt += 1
print(max(A) - cnt)
