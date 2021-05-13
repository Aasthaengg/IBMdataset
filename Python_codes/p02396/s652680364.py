import warnings


n = 0
i = 0
while (n == 0): 

	i = i + 1

	data = input()
	if(data == 0):
		break
	else:
		print "Case " + str(i) + ": " + str(data)