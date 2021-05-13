n,k = map(int,input().split())
v = list(map(int,input().split()))
ma = 0
kaisu = min(n,k)
for a in range(kaisu+1):
    for b in range(kaisu-a+1):
        push = k-(a+b)
        li = v[:a]+v[n-b:]
        li.sort(reverse=True)
        for c in range(push):
            if li:
                if li[-1] < 0:
                    li.pop()
        ma = max(ma,sum(li))
print(ma)