string_list = input().split(' ')
D = int(string_list[0])
T = int(string_list[1])
S = int(string_list[2])
kyori = T * S
if D<=kyori:
  print('Yes')
else:
  print('No')