n=input()
for i in range(n):
	if i==0:
		num_1=input()
	elif i==1:
		num_2=input()
		maxv=num_2 - num_1
		MIN=min(num_1,num_2)
	else:
		num_3=input()
		if (num_3-MIN)>maxv:
			maxv=num_3-MIN
		if (num_3)<MIN:
			MIN=num_3
print(maxv)