n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [0]*(n+1)
B = [0]*(m+1)
cnt  =0

for i in range(1,n+1):
    A[i] = A[i-1] + a[i-1]
for i in range(1,m+1):
    B[i] = B[i-1] + b[i-1]

j = m
for i in range(n+1):
    if A[i] > k:
        break
    while B[j] + A[i] > k:
        j -= 1
    cnt = max(cnt, i + j)

print(cnt)