input_line = raw_input().split()

a = int(input_line[0])
b = int(input_line[1])

if(a<b):
	print 'a < b'
elif(a>b):
	print 'a > b'
else:
	print 'a == b'