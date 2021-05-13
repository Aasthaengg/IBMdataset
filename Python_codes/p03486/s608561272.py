s = input()
t = input()
s_min = ''.join(sorted(s))
t_max = ''.join(sorted(t, reverse = True))
if s_min < t_max:
    print('Yes')
else:
    print('No')