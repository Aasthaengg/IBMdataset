N = int(input())
A = [int(i) for i in input().split()]
cnt = 0
for i in range(N):
    a = A[i]
    if A[a - 1] < a:
        continue
    if A[a - 1] - 1 == i:
        cnt += 1
print(cnt)
