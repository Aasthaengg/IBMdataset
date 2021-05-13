characters = list(input())
n = int(input())
for i in range(n):
  order_list = list(map(str, input().split()))
  order_list[1] = int(order_list[1])
  order_list[2] = int(order_list[2])
  if order_list[0] == 'replace':
    for j in range(order_list[1], order_list[2]+1):
      characters[j] = order_list[3][j-order_list[1]]
  if order_list[0] == 'reverse':
    sliced_part = characters[order_list[1]:order_list[2]+1]
    sliced_part = sliced_part[::-1]
    for j in range(order_list[1], order_list[2]+1):
      characters[j] = sliced_part[j-order_list[1]]
  if order_list[0] == 'print':
    for i in range(order_list[1], order_list[2]+1):
      print(characters[i], end='')
    print('')
