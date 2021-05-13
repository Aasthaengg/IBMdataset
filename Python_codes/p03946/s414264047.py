N, T = map(int,input().split())
A = list(map(int,input().split()))
MIN = A[0]
ans = 0
diff = 0
for i in range(1, N):
    if MIN > A[i]:
        MIN = A[i]
    elif A[i] - MIN > diff:
        ans = 1
        diff = A[i] - MIN
    elif A[i] - MIN == diff:
        ans += 1

print(ans)