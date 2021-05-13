tt = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

p = (aa[0] - bb[0]) * tt[0]
q = (aa[1] - bb[1]) * tt[1]

if p > 0:
	p *= -1
	q *= -1

if p + q < 0:
	print(0)
elif p + q == 0:
	print("infinity")
else:
	r, s = divmod((-1 * p), (p + q))
	if s == 0:
		print(r * 2)
	else:
		print(r * 2 + 1)