import warnings

data = map(int, raw_input().split())

a = data[0]
b = data[1] + 1
c = data[2]

count = 0
for i in range(a, b):
	if(c % i == 0):
		count = count + 1
#		print i

#print "The number of divisor is:" + str(count)
print count