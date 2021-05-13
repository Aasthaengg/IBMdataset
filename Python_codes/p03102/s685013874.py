import numpy

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
B = numpy.array(B)

ans = 0
for _ in range(N):
    a = numpy.array(list(map(int, input().split())))
    if numpy.dot(a, B) + C > 0:
        ans += 1

print(ans)