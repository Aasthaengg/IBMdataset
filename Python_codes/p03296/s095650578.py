N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 1):
    if A[i] == -1:
        continue
    if A[i] == A[i + 1]:
        A[i + 1] = -1
        cnt += 1
print(cnt)
