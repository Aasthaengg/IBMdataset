N = int(input())

A = list(map(int, input().split()))

ans = 0
max = 0

for i in range(N):
    if max < A[i]:
        max = A[i]
    else:
        ans += max - A[i]

print(ans)