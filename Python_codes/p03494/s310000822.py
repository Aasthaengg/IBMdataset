def calc_num2(num):
  total = 0
  while num % 2 == 0:
    total += 1
    num = num / 2
  
  return total

num_count = input()
num_list = [int(i) for i in input().split(' ')]
ans_list = []
for num in num_list:
  ans_list.append(calc_num2(num))

print(min(ans_list))