import warnings


number = input()

array = map(int, raw_input().split())

num_max = array[0]

num_min = array[0]

data_sum = 0

#print len(array)

for i in range(len(array)):
	
	data_sum = data_sum + array[i]

	if array[i] < num_min: 
		num_min = array[i]
	
	if array[i] > num_max:
		num_max = array[i]

print num_min, num_max, data_sum