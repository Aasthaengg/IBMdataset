import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count = 0

A.sort()
C.sort()

for i in B:
    t = bisect.bisect_left(A,i)
    s = N - bisect.bisect_right(C,i)
    count += t*s
print(count)