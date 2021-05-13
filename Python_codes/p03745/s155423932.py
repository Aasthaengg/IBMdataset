N = int(input())
A = list(map(int,input().split()))
A = A
f = 0
ans = 1
for k in range(N-1):
    if f == 0:
        if A[k] > A[k+1]:
            f = -1
        elif A[k] < A[k+1]:
            f = 1
    elif f == 1:
        if A[k] > A[k+1]:
            ans += 1
            f = 0
    else:
        if A[k] < A[k+1]:
            ans += 1
            f = 0
print(ans)
