input_data = [int(i) for i in input().split()]

a = input_data[0]
b = input_data[1]
c = input_data[2]

count=0
for i in range(a,b+1):
	if c % i == 0:
		count +=1

print(count)