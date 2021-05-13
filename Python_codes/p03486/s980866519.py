s = input()
t = input()
l_s = [s[i] for i in range(len(s))]
l_t = [t[i] for i in range(len(t))]
l_s.sort()
l_t.sort(reverse=True)
s_new = ''.join(l_s)
t_new = ''.join(l_t)
if s_new < t_new:
  print('Yes')
else:
  print('No')