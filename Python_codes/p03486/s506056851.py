s=list(input())
t=list(input())

s.sort()
t.sort()
t.reverse()

s_a=''.join(s)
t_a=''.join(t)

if s_a<t_a:
  print('Yes')
else:
  print('No')