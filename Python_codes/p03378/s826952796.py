n,m,x = map(int,input().split())
a = list(map(int,input().split()))
import bisect
c = bisect.bisect(a,x)
print(min(c,m-c))