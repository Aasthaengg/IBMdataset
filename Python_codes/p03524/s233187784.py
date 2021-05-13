S = input()
s_dict = {'a': 0, 'b': 0, 'c': 0}
for s in S:
  s_dict[s] += 1
if max(s_dict.values())-min(s_dict.values()) > 1:
  print('NO')
else:
  print('YES')
