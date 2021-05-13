n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(0, n-1):
    if A[i] + A[i+1] > x:
        diff = A[i] + A[i+1] - x
        ans += diff
        A[i+1] = max(0, A[i+1]-diff)

print(ans)
