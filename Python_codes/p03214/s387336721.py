N = int(input())
A = list(map(int, input().split()))
import numpy
B = numpy.array(A)
b = numpy.average(A)
ans = 0
dif = abs(A[0] - b)
for i in range(1, N):
    a = abs(A[i] - b)
    if a < dif:
        dif = a
        ans = i
print(ans)