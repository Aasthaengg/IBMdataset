import bisect

n = int(input())
A = list(map(int, input().split()))
A.sort()
ama = A[-1]
print(ama, end=' ')
ama2 = (ama + 1)//2
w = bisect.bisect_left(A, ama2)

a = A[w-1]
b = A[w]
if abs(a-ama2) > abs(b-ama2):
    print(b)
else:
    print(a)
