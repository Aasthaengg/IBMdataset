a = input()
b = int(input())

c = ''
for i in range(len(a)):
	if(i%b == 0):
		c += a[i]
		
print (c)