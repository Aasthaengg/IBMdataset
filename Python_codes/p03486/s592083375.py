s = input()
t = input()

s_asc = ''.join(sorted(s))
t_desc = ''.join(sorted(t, reverse=True))
print('Yes' if s_asc < t_desc else 'No')