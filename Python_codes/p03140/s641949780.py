
N = int(input())
A = str(input())
B = str(input())
C = str(input())


ans = 0

for i in range(N):
    if A[i] is B[i] and A[i] is C[i]:
        pass
    elif A[i] is B[i] and B[i] is not C[i] and A[i] is not C[i]:
        ans += 1
    elif B[i] is C[i] and B[i] is not A[i] and C[i] is not A[i]:
        ans += 1
    elif A[i] is C[i] and A[i] is not B[i] and C[i] is not B[i]:
        ans += 1
    else:
        ans += 2

print(ans)