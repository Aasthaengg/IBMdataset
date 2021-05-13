import numpy

N = int(input())
A, B = numpy.array([list(map(int, input().split())) for _ in range(N)]).T

A = A[::-1]
B = B[::-1]

ans = 0
for i in range(N):
    a, b = A[i], B[i]

    # need to do nothing
    if (a + ans) % b == 0:
        continue

    else:
        ans += b - (a + ans) % b

print(ans)