s = input()
s_n = ''.join(sorted(s))

t = input()
t_n = ''.join(sorted(t,reverse = True))

if s_n < t_n:
  print('Yes')

else:
  print('No')
