N = int(input())
A = list(map(int, input().split()))
allL = sum(A)
L, mL = 0, float('inf')
for i in range(N):
    L += A[i]
    if abs(2*L-allL) < mL:
        mL = abs(2*L-allL)
    else:
        break
print(mL)