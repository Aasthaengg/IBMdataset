import bisect
n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
a_ = bisect.bisect_right(p,a)
b_ = bisect.bisect_right(p,b)
print(min(a_,b_-a_,n-b_))