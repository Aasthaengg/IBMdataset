k, t = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
if sum(A[:t-1]) >= A[-1]:
    print(0)
else:
    print(A[-1]-sum(A[:t-1])-1)