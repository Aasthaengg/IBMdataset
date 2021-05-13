n = int(input())
num_list = [int(i) for i in input().split()]
if len(num_list)==1:
  print(1)
else:
  res = 1
  flag = None
  pre = num_list[0]
  for i in num_list[1:]:
    if pre > i and not flag:
      flag = 'down'
  
    elif pre < i and not flag:
      flag = 'up'
      
    elif (pre > i and flag=='up') or (pre < i and flag=='down'):
      res += 1
      flag = None
    pre = i
  print(res)