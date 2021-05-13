n = int(input())
A = [int(input()) for i in range(n)]

ng = 0
if A[0] != 0:
    ng = 1
ans = 0
for i in range(1, n):
    if A[i] > A[i-1] and A[i] - A[i-1] > 1:
        ng = 1
        break
    elif A[i] <= A[i-1]:
        ans += A[i]
    else:
        ans += 1

if ng == 0:
    print(ans)
else:
    print(-1)