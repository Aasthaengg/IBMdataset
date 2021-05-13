N = int(input())
A = []
for _ in range(N):
    b = int(input())
    A.append(b)

B = sorted(A)
mfirst = B[-1]
msecond = B[-2]

for i in range(N):
    if A[i] == mfirst:
        print(msecond)
    else:
        print(mfirst)
