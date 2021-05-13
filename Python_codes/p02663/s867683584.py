input_str = input().split()

input_nums=[]

for i in range(5):
    input_nums.append(int(input_str[i]))


diff_hour = input_nums[2] - input_nums[0]
diff_hour_to_min = diff_hour * 60
 
diff_min = input_nums[3] - input_nums[1]

total_wake_min = diff_hour_to_min + diff_min

print(total_wake_min - input_nums[4])