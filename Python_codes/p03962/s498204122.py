sample = input()
sample_list = sample.split(" ")
count = 0
flag = 0
i = 0
j = 1
for i in range(len(sample_list)):
  for j in range(i):
    if sample_list[i] == sample_list[j]:
      flag = 1
  if flag == 0:
    count += 1
  flag = 0
print(count)
