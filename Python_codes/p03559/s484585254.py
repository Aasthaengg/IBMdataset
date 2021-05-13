n=int(input())
a=sorted(list(map(int,input().split())))
b=list(map(int,input().split()))
c=sorted(list(map(int,input().split())))
import bisect
ans=0
for i in range(n):
    inda=bisect.bisect_left(a,b[i])
    indc=bisect.bisect_right(c,b[i])
    ans += inda*(n-indc)
print(ans)