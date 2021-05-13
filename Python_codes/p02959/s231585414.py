N = int(input())
C = tuple(map(int,input().split()))
B = list(map(int,input().split()))
A = list(C)
for i in range(N)[::-1]:
    if A[i+1] > B[i]:
        A[i+1] -= B[i]
    elif B[i] < A[i]+A[i+1]:
        A[i] -= (B[i] - A[i+1])
        A[i+1] = 0
    else:
        A[i] = 0
        A[i+1] = 0
ans = 0
for j in range(N+1):
    ans += C[j]-A[j]
print(ans)