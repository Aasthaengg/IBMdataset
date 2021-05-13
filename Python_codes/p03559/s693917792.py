import bisect
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
lenc = len(c)
a.sort()
c.sort()
ans = 0
for i in b:
	atmp = bisect.bisect_left(a, i)
	ctmp = lenc - bisect.bisect_right(c, i)
	ans += atmp * ctmp
print(ans)