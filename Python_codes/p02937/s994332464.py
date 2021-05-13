s = input()
t = input()
len_s = len(s)
a = ord('a')
dictionary = {chr(a + i): [[], 0] for i in range(26)}
for i in range(len_s):
  dictionary[s[i]][0].append(i)
  dictionary[s[i]][1] += 1
repeat = 0
cur_index = -1
for c in t:
  indices, len_indices = dictionary[c]
  if len_indices == 0:
    repeat = 0
    cur_index = -2
    break
  inf = -1
  sup = len_indices
  while sup - inf > 1:
    x = (inf + sup) // 2
    if indices[x] > cur_index:
      sup = x
    else:
      inf = x
  if sup == len_indices:
    repeat += 1
    cur_index = indices[0]
  else:
    cur_index = indices[sup]
print(len_s * repeat + cur_index + 1)