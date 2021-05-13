m,f,r = [],[],[]
grade = []
while True:
	a,b,c = map(int,input().split())
	if a == -1 and b == -1 and c == -1:
		break
	else:
		m.append(a)
		f.append(b)
		r.append(c)
for i in range(len(m)):
	if m[i] == -1 or f[i] == -1:
		grade.append("F")
	elif m[i] + f[i] >= 80:
		grade.append("A")
	elif m[i] + f[i] >= 65:
		grade.append("B")
	elif m[i] + f[i] >= 50 or r[i] >= 50:
		grade.append("C")
	elif m[i] + f[i] >= 30:
		grade.append("D")
	else:
		grade.append("F")
for k in grade:
	print(k)
