import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

total = 0
for i in range(N):
    a = bisect.bisect_left(A,B[i])
    c = N - bisect.bisect_right(C,B[i])
    total += a*c

print(total)