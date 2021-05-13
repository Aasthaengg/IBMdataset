num = int(input())
x=""

for i in range(1,num+1):
	if str(i).find("3") != -1:
		x += (" " + str(i))
	elif i % 3 == 0:
		x += (" " + str(i))
print(x)