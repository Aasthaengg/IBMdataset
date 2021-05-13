n,m,k = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

for i in range(n):
    A[i+1] += A[i]

for i in range(m):
    B[i+1] += B[i]

ans = 0
j = m

for i in range(n+1):
    if A[i] > k:
        continue

    while A[i] + B[j] > k:
        j -= 1

    ans = max(ans,j+i)

print(ans)