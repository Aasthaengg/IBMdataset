import bisect

N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

num = bisect.bisect_left(A, X)

result = min(M-num, num)

print(result)