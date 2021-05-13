c = [0]*3
for i in range(3):
	c[i] = input()
L = []
for i in range(3):
	b = list(c[i])
	L.append(b[i])
print(''.join(L))