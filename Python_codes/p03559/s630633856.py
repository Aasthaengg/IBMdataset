import bisect
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
c.sort()
ans=0
for i in b:
    ai=bisect.bisect_left(a,i)
    ci=bisect.bisect_right(c,i)
    ans+=ai*(n-ci)
print(ans)