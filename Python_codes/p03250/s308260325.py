num_list = list(map(int,input().split()))
max_num = max(num_list)
f_max = 0
sum_result = 0
for i in num_list:
	if i == max_num and f_max == 0:
		sum_result = sum_result + 10 * i
		f_max = 1
	else:
		sum_result = sum_result + i
		
print(sum_result)