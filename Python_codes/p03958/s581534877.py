k,t = map(int, input().split())
lis = list(map(int, input().split()))

m = max(lis)
lis = sorted(lis)

if lis[-1:]:
    pass

if sum(lis[:-1]) >= m:
    print(0)
else:
    print(m-1-sum(lis[:-1]))
