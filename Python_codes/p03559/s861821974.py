import bisect as bi

N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a.sort()
c.sort()
#print(a)
#print(c)

ans=0
for i in b:
  ans+=bi.bisect_left(a,i)*(N-bi.bisect_right(c,i))
print(ans)