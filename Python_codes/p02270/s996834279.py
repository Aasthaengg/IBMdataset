n,k = map(int,input().split())
w = []
for i in range(n):
	w.append(int(input()))
s = sum(w)
m = max(w) - 1
while (s-m) > 1:
	mid = (s+m+1)//2
	tmp = 0
	c = 0	
	for i in w:
		if tmp+i > mid:
			tmp = i
			c += 1
		else:
			tmp += i
	if c < k:
		s = mid
	else:
		m = mid
print(s)
