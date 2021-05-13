import copy
 
kaisu = int(input())
 
s_suji_list = input().split(' ')
suji_list = []
count = 1
continue_flg = True
for suji in s_suji_list:
  i_suji = int(suji)
  if i_suji % 2 == 0:
    suji_list.append(i_suji / 2)
  else:
    continue_flg = False
    count = 0
    break
 
while(continue_flg):
  temp_list = copy.copy(suji_list)
  suji_list.clear()
  count += 1
  for suji in temp_list:
    if suji % 2 == 0:
      suji_list.append(suji / 2)
    else:
      count -= 1
      continue_flg = False
      break
 
print(count)