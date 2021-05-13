numbers = [i for i in map(int, input().split())]
number_list = [i+numbers[0] for i in range(numbers[1]-numbers[0]+1)]
count = 0
for i in number_list:
  if i % numbers[2] == 0:
    count+=1
print(count)
