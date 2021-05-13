n = int(raw_input())
tp,hp = 0,0
for i in range(n):
	T,H = raw_input().split(' ')
	if T == H :
		tp += 1
		hp += 1
	elif T > H :
		tp += 3
	else:
		hp += 3
print tp,hp 