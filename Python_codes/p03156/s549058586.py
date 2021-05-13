import bisect
n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
x = bisect.bisect_left(p,a+1)
y = bisect.bisect_left(p,b+1)
one = p[:x]
two = p[x:y]
three = p[y:]
print(min(len(one),len(two),len(three)))