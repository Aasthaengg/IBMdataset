n = input()

a = 9*(len(n)-1)

b = 0
for i in n:
	b += int(i)

c = 0
for i in range(len(n)):
	if i == 0:
		c += int(n[i])-1
	else:
		c += 9
print (max(a,b,c))