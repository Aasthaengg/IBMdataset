s = input()
s_sort = ''.join(sorted(s))

t = input()
t_sort = ''.join(sorted(t, reverse=True))

if s_sort < t_sort:
  print('Yes')
else:
  print('No')