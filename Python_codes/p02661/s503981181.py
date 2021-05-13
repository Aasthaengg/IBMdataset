N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
    medi = N // 2
    ans = B[medi] - A[medi] + 1
else:
    medi1 = N // 2 - 1
    medi2 = medi1 + 1
    A_medi = (A[medi1] + A[medi2]) / 2
    B_medi = (B[medi1] + B[medi2]) / 2
    ans = (B_medi - A_medi) * 2 + 1
print(int(ans))
