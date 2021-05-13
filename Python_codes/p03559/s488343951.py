import bisect

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()

count = 0

for i in range(len(B)):
    a_b = bisect.bisect_left(A,B[i])
    c_b = bisect.bisect_right(C,B[i])
    count += a_b * (N - c_b)

print(count)