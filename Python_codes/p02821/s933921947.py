n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
b = a[::-1] #小さい順

upper = 200001
lower = 1
while upper-lower > 1:
	mid = (upper+lower)//2
	cnt = 0
	ma = 0
	for mi in range(n):
		while ma < n and b[mi] + a[ma] >= mid:
			ma += 1
		cnt += ma
		#print(ma, mi)
	#print(lower, mid, upper, cnt)
	if cnt > m:
		lower = mid
	else:
		upper = mid

uppercnt = []
cnt = 0
for i in range(n):
	while (cnt < n-1) & (a[i] + b[cnt] < upper):
		cnt += 1
	if a[i] + b[cnt] >= upper:
		uppercnt.append(cnt)
	else:
		uppercnt.append(-1)
c = [a[0]]

uppernum = 0
for i in range(n-1):
	d = c[i] + a[i+1]
	c.append(d)
for i in range(n):
	if uppercnt[i] == -1:
		continue
	else:
		#print(a[i], (n-uppercnt[i]))
		#print(c[n-uppercnt[i]-1])
		uppernum += a[i] * (n-uppercnt[i])
		uppernum += c[n-uppercnt[i]-1]
uppercnter = 0
for i in uppercnt:
	if i != -1:
		uppercnter += n-i

print(lower*(m-uppercnter)+uppernum)