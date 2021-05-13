import bisect
N,M,X = map(int,input().split())
A = list(map(int,input().split()))

ans_N = M - bisect.bisect_left(A,X)
ans_0 = bisect.bisect_left(A,X)
print(min(ans_N,ans_0))