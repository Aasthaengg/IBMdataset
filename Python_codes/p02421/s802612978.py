t = int(input())
q,w = 0,0
for i in range(t):
	a,b = input().split()
	if a == b:
		q += 1
		w += 1
	elif a<b :
		w+=3
	elif a>b:
		q+=3
print(q,w)

