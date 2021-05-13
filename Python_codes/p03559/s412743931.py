import bisect
N = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))
ans = 0
for i in b:
	a2 = bisect.bisect_left(a,i)
	c2 = len(c) - bisect.bisect_right(c,i)
	ans += a2 * c2
print(ans)
