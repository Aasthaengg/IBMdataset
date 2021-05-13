import bisect
X = int(input())
A = [599, 799, 999, 1199, 1399, 1599, 1799, 1999]
ans = bisect.bisect_left(A, X)
print(8 - ans)