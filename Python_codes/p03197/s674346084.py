
N = int(input())

A = []

for i in range(N):

    a = int(input())
    A.append(a)

A.sort()

ans = 0
las = 0

for i in range(N):

    if (A[i] - las) % 2 != 0:
        ans ^= N - i

    las = A[i]

if ans == 0:
    print ("second")
else:
    print ("first")

