import bisect

n = int(input())
A = sorted(list(map(int,input().split())))
ma = A[-1]
half = ma / 2
index = bisect.bisect_left(A,half)

if index != 0:
    ans = A[index-1] if half - A[index-1] <= A[index] - half else A[index]
else:
    ans = A[0]

print(ma,ans)