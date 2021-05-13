num_list = [i for i in range(4)]
for j in range(4):
  num_list[j] = int(input())
print(min(num_list[0],num_list[1])+min(num_list[2],num_list[3]))