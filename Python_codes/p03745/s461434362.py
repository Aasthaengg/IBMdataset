N = int(input())
A = list(map(int,input().split()))
ans = 1
cur = 'N'
i = 1
while i < N:
    if cur == 'U':
        if A[i] < A[i-1]:
            ans += 1
            cur = 'N'
        i += 1
    elif cur == 'D':
        if A[i] > A[i-1]:
            ans += 1
            cur = 'N'
        i += 1
    elif cur == 'N':
        if A[i] > A[i-1]:
            cur = 'U'
        elif A[i] < A[i-1]:
            cur = 'D'
        i += 1
print(ans)