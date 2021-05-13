def check(mid):
	val = 0
	for i in c:
		if(i[0]*i[1] > mid):
			val += i[0] - (mid//i[1])
	return val <= k

def bs():
	l = 0
	r = 1e18
	while(l <= r):
		mid = (l+r)//2
		if(check(mid)):
			r = mid-1
		else:
			l = mid+1
	return r+1

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse = True)
c = [[a[i],b[i]] for i in range(n)]
print(int(bs()))