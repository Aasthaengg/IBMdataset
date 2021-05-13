import bisect

N = int(input())
A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]
C = [int(i) for i in input().split(' ')]

A.sort()
B.sort()
C.sort()

count = 0
for b in B:
    i = bisect.bisect_left(A,b)
    j = bisect.bisect_right(C,b)
    count += i * (N - j)

print(count)