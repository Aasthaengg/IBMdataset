import sys

N = int(input())

A = []

for i in range(N):

    a = int(input())
    A.append(a)

if A[0] != 0:
    print (-1)
    sys.exit()

A.reverse()

ans = 0

for i in range(N):

    if i == 0:
        ans += A[i]

    else:

        if A[i-1] - 1 > A[i]:
            print (-1)
            sys.exit()

        elif A[i-1] -1 == A[i]:
            pass

        else:
            ans += A[i]

print (ans)
