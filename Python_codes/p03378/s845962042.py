import bisect
N,M,X = map(int,input().split())
a = list(map(int, input().split()))
l = bisect.bisect_left(a, X)
print(min(l, M-l))