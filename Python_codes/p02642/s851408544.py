N = int(input())
A = list(map(int, input().split()))

A = sorted(A, key=lambda x: x)
all = [True] * 1000001
ans = 0
for i in range(N):
    if all[A[i]] == False:
        continue
    if i == N - 1 or A[i+1] > A[i]:
        ans += 1
    b = A[i]
    while b < 1000001:
        all[b] = False
        b += A[i]

print(ans)