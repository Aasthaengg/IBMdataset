n, w = map(int, input().split())
list_item = []
for _ in range(n):
  weight, value = map(int, input().split())
  list_item.append((weight, value))

dict_ks = {}
dict_ks[0] = 0
num_checked = 0
while num_checked < n:
  new_w, new_v = list_item[num_checked]
  for temp_w, temp_v in list(dict_ks.items()):
    if temp_w + new_w <= w:
      if temp_w + new_w not in dict_ks:
        dict_ks[temp_w + new_w] = temp_v + new_v
      else:
        dict_ks[temp_w + new_w] = max(dict_ks[temp_w + new_w], temp_v + new_v)
  num_checked += 1

print(max(dict_ks.values()))