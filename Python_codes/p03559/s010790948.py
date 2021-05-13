import bisect
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
c.sort()
ans=0
for i in b:ans+=bisect.bisect_left(a,i)*(n-bisect.bisect_right(c,i))
print(ans)