words = input()

lst = ['A', 'C', 'G', 'T']
max_count = 0
count = 0
for i in range(len(words)):
  if words[i] in lst:
    count += 1
    if i == len(words) - 1:
      if count > max_count:
        max_count = count
  else:
    if count > max_count:
      max_count = count
    count = 0
print(max_count)
