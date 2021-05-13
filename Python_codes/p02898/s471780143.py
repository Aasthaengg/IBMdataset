import bisect
N,K =list(map(int,input().split()))
H =sorted(list(map(int,input().split())))
i = bisect.bisect(H,K-1)
print(N-i)