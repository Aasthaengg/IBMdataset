from bisect import bisect_right

n, m, x = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
index = bisect_right(A, x)
print(min(len(A[:index]), len(A[index:])))