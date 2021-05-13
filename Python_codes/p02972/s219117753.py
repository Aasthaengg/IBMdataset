N = int(input())
A = list(map(int,input().split()))

B = [0] * N
for i in range(N-1,-1,-1):
    n = 1
    SUM = 0
    while (i+1) * n < N+1:
        m = (i+1) * n -1
        SUM += B[m]
        n += 1
    if SUM % 2 == A[i]:
        B[i] = 0
    else:
        B[i] = 1

ans = []
for i,b in enumerate(B):
    if b == 1:
        ans.append(i+1)
print(len(ans))
print(*ans)
