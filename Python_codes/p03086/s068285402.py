s = input()
count = 0
lens = []

for i, _ in enumerate(s):
  for c in s[i:]:
    if c in ['A', 'G', 'C', 'T']:
      count += 1
    else:
      break
  lens.append(count)
  count = 0
  
print(max(lens))
  
