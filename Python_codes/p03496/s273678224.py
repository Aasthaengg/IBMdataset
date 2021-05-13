N = int(input())
A = [int(a) for a in input().split()]
maxi, maxA, mini, minA = 0, A[0], 0, A[0]
for i in range(1, N):
    if A[i] > maxA: maxi, maxA = i, A[i]
    if A[i] < minA: mini, minA = i, A[i]

Ans = []
if abs(maxA) >= abs(minA):
    for i in range(N):
        if A[i] < 0:
            Ans.append((maxi+1, i+1))
            A[i] += maxA
    for i in range(1, N):
        if A[i] < A[i-1]:
            Ans.append((i, i+1))
            A[i] += A[i-1]
else:
    for i in range(N):
        if A[i] > 0:
            Ans.append((mini+1, i+1))
            A[i] += minA
    for i in reversed(range(N-1)):
        if A[i] > A[i+1]:
            Ans.append((i+2, i+1))
            A[i] += A[i+1]

print(len(Ans))
for x, y in Ans:
    print(x, y)