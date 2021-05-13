import bisect
n,m,x = map(int,input().split())
a = [int(i) for i in input().split()]
b = bisect.bisect(a,x)
#print(b,m-b)
print(min(b,m-b))
