last = 0
answer = 0
dishes = []
dishes.append(int(input()))

for i in range(1,5):
	dish = int(input()) 
	dishes.append(dish)
	if dish % 10 != 0 and dishes[last] % 10 >  dish % 10:
		last = i


for i in range(5):
	if i == last:
		answer += dishes[i]
	else:
		if dishes[i] % 10 == 0:
			answer += dishes[i] 
		else:
			answer += ((dishes[i]//10)+1)*10

print(answer)