import collections
h = collections.Counter([0])
cumul,m,ans = 0,2019,0
pt = 1
for j,u in enumerate(map(int,list(raw_input()))[::-1]):
	cumul += u * pt
	cumul %= m
	pt *= 10
	pt %= m
	ans += h[cumul]
	h[cumul]+=1
print ans

