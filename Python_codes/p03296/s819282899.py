N = int(input())
A = [int(i) for i in input().split()]

cnt = 0
for i in range(1, N):
    if A[i] == A[i-1]:
        A[i] = -1
        cnt += 1

print(cnt)