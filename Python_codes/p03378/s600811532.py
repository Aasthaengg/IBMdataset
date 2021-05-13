import bisect
n,m,x = map(int,input().split())
a = list(map(int,input().split()))
#aa = sorted(a,reverse=True)

#print(bisect.bisect_left(a,x))
#print(bisect.bisect_left(aa,x))

left = bisect.bisect_left(a,x)
print(min(left,len(a)-left))