long_str = input()
short_str = input()
short_list = list(short_str)

long_len = len(long_str)
short_len = len(short_str)
iter_num = long_len - short_len + 1

max_count = 0
for i in range(iter_num):
  tmp = 0
  obj_list = list(long_str[i:(short_len+i)])
  for s, o in zip(short_list, obj_list):
    tmp += int(s == o)
  max_count = max(max_count, tmp)

print(short_len - max_count)
