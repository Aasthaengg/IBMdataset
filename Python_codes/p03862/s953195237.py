n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if A[i-1]+A[i] <= x:
        continue
    eat = A[i-1]+A[i] - x
    ans += eat
    A[i] = max(0, A[i]-eat)

print(ans)