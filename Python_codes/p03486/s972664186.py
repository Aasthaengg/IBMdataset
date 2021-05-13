s = input()
t = input()

s_list = [i for i in s]
t_list = [i for i in t]
s_list.sort()
t_list.sort()
t_list.reverse()
s = ''.join(s_list)
t = ''.join(t_list)

if s < t:
  print('Yes')
else:
  print('No')