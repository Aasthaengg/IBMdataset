# import sys
matches = input()
matches_list = list(matches)
# o = 0
x = 0
for i in matches_list:
  # if i == 'o':
  #   o += 1
  if i == 'x':
    x += 1

if x >= 8:
  print('NO')
else:
  print('YES')
  # sys.exit()

# print(x, matches_list)