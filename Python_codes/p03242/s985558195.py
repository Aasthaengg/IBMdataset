n = input()
output = []

for i in n:
	if i == "1":
		output.append("9")
	elif i =="9":
		output.append("1")
	else:
		output.append(i)
		
print("{}{}{}".format(output[0],output[1],output[2]))