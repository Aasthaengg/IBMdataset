import bisect
n = int(input())
a,b = map(int,input().split())
P = list(map(int,input().split()))
P.sort()
x = bisect.bisect_right(P, a)
y = bisect.bisect_right(P, b)
print(min(x, y-x, n-y))
