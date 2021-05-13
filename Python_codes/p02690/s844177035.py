X=int(input())
A_max=120
B_max=119
A_min=-119
B_min=-120
for i in range(-119,120):
	for j in range(-120,119):
		if i**5-j**5==X:
			print(i,j)
			break
	else:
		continue
	break