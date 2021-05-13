n = int(input())
a = list(map(int, input().split()))
dict = {}
b = [0,0]
c = [0,0]
for i in a:
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1
	if dict[i] == 2:
		b.append(i)
	if dict[i] == 4:
		c.append(i)
b.sort(reverse=True)
c.sort(reverse=True)
print (max(b[0] * b[1],c[0]**2))