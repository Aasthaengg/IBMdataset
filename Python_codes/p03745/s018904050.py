N = int(input())
A = list(map(int, input().split()))
i = 0
ans = 0
while i < N:
    if i == N-1:
        ans += 1
        break
    if A[i] == A[i+1]:
        i += 1
    elif A[i] > A[i+1]:
        while i < N-1 and A[i] >= A[i+1]:
            i += 1
        ans += 1
        i += 1
    elif A[i] < A[i+1]:
        while i < N-1 and A[i] <= A[i+1]:
            i += 1
        ans += 1
        i += 1
    

print(ans)