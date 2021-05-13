n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == 0:
        if A[i] <= x:
            continue
        eat = A[i] - x
        ans += eat
        A[i] = A[i] - eat
        continue
    if A[i-1]+A[i] <= x:
        continue
    eat = A[i-1] + A[i] - x
    ans += eat
    A[i] = A[i] - eat

print(ans)