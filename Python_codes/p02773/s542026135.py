import collections

N = int(input())
S_list = []
for n in range(N):
  S_list.append(input())

c = collections.Counter(S_list)
max_list = []
_max_value = 0
for idx, value in enumerate(c.most_common()):
  if idx == 0:
    max_list.append(value[0])
    _max = value[1]
    continue
  if _max == value[1]:
    max_list.append(value[0])
  else:
    break

for answer in sorted(max_list):
  print(answer)