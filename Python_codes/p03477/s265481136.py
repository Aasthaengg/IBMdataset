num_list = list(map(int, input().split()))
if(num_list[0]+num_list[1]>num_list[2]+num_list[3]):
	print("Left")
elif(num_list[0]+num_list[1]==num_list[2]+num_list[3]):
	print("Balanced")
else:
	print("Right")