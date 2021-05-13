number = int(input())
count = 0

for i in range(1,number):
  temp = number -1
  temp_solution = int(temp/i)
  count += temp_solution
print(count)