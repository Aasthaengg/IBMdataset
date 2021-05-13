N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

prev = -2
ans = 0
for i in range(len(A)):
    if A[i] == prev+1:
        ans += C[prev-1]
    ans += B[A[i]-1]
    prev = A[i]

print(ans)