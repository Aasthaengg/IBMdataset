n,m,c = map(int, input().split())
B = list(map(int, input().split()))

cnt = 0
for i in range(n):
    judge = 0
    A = list(map(int, input().split()))
    for j in range(m):
        judge += A[j]*B[j]
    if judge + c > 0:
        cnt += 1
print(cnt)