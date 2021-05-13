h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
hw = [[0 for i in range(w)] for j in range(h)]

k = 0
l = 0
ary = []
for i in range(n):
	loop = a[i]
	j = 0
	b = [i+1 for j in range(a[i])]
	ary.extend(b)
c = 0
for i in range(0,h*w,w):
	if c%2 == 1:
		d = ary[i:i+w]
		del ary[i:i+w]
		d.reverse()
		ary[i:i] = d
	e = ary[i:i+w]
	print (*e)
	c += 1