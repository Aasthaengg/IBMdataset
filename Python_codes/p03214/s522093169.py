N = int(input())
A = list(map(int, input().split()))
avg = sum(A) / N

d = float('inf')
ans = 0
for i in range(N):
    if d > abs(A[i] - avg):
        d = abs(A[i] - avg)
        ans = i
print(ans)