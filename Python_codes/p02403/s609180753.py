data_h = []
data_w = []
while True:
	h, w = (int(i) for i in input().split())
	if h == 0 == w:
		break
	else:
		data_h.append(h)
		data_w.append(w)

#print(data_h, data_w)
#print(len(data_h),len(data_w))

for count in range(len(data_h)):
	h = data_h[int(count)]
	w = data_w[int(count)]
	for i in range(h):
		for j in range(w):
			print('#',end='')
		print('')
	print('')