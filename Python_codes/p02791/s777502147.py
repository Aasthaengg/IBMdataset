N = int(input());
p_list = list(map(int, input().split()));

min = p_list[0];
count = 0;
for i in range(len(p_list)):
  if (min >= p_list[i]):
    count += 1;
    min = p_list[i];

print(count);