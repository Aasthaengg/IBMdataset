import bisect
N, K = map(int, input().split())
Nlist = list(map(int, input().split()))
Nlist.sort()
okindex = bisect.bisect_left(Nlist, K)
print(N-okindex)
