list_a = [1, 3, 5, 7, 8, 10, 12]
list_b = [4, 6, 9, 11]
list_c = [2]

x, y = map(int, input().split())
if (x in list_a and y in list_a) or (x in list_b and y in list_b) or (x in list_c and y in list_c):
  print('Yes')
else:
  print('No')