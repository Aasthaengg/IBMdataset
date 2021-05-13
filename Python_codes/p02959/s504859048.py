N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Ans = 0
for i in range(N):
    if A[i] + A[i+1] < B[i]:
        Ans += A[i] + A[i+1]
        A[i+1] = 0
    elif A[i] >= B[i]:
        Ans += B[i]
    else:
        Ans += B[i]
        A[i+1] -= B[i] - A[i]
print(Ans)