from itertools import product
h, w, k = map(int, input().split())
s = list()
best_so_far = float('inf')
for _ in range(h):
  line = input()
  s.append(list(map(int, list(line))))
# loop over possible horizontal lines, 2**9=512 possibilities
horizontal_line_choices = product([False, True], repeat=h-1)
for chosen_indices in horizontal_line_choices:
  hyperrow_values = [s[0].copy()]
  for i in range(h-1):
    if chosen_indices[i]:
      hyperrow_values.append(s[i+1].copy())
    else:
      for dw in range(w):
        hyperrow_values[-1][dw] += s[i+1][dw]
  if any(value>k for row in hyperrow_values for value in row):
    continue
  # now got hyperrow_values, do a greedy search on vertical lines
  num_hyperrows = len(hyperrow_values)
  count_cuts = sum(chosen_indices)
  hyperrow_cumulative = [hyperrow_values[r][0] for r in range(num_hyperrows)]
  for j in range(1, w):
    if all(hyperrow_cumulative[r]+hyperrow_values[r][j]<=k for r in range(num_hyperrows)):
      for r in range(num_hyperrows):
        hyperrow_cumulative[r] += hyperrow_values[r][j]
    else:
      count_cuts += 1
      for r in range(num_hyperrows):
        hyperrow_cumulative[r] = hyperrow_values[r][j]
  best_so_far = min(best_so_far, count_cuts)
print(best_so_far)