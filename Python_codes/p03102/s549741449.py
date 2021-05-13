N,M,C = map(int, input().split())
B = tuple(map(int,input().split()))
A = []
for i in range(N):
    A.append(tuple(map(int,input().split())))

ans = 0
for i in A:
    judge = 0
    for j in range(M):
        judge += i[j]*B[j]
    judge += C
    if judge > 0:
        ans += 1
print(ans)
