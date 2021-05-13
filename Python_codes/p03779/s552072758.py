import bisect
n = int(input())
sl = []
for i in range(1,100000):
	sl.append(i*(i-1)//2+1)
ans = bisect.bisect_right(sl, n)
print(ans)