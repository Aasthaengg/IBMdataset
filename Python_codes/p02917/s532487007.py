N = int(input())
B = list(map(int, input().split()))

A = []
ans = 0
for i in range(N-1):
    if i == 0:
        A.append(B[i])
        continue
    if B[i] >= B[i-1]:
        A.append(B[i-1])
    else:
        A.append(B[i])
A.append(B[N-2])
for i in range(N):
    ans += A[i]

print(ans)