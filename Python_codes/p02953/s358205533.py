n = int(input())
lst = [0] + list(map(int, input().split()))
reach = False
for i in range(n):
  if reach:
    if lst[i + 1] - lst[i] <= -1:
      print('No')
      exit()
    elif lst[i + 1] - lst[i] >= 1:
      reach = False
  else:
    if lst[i + 1] - lst[i] == -1:
      reach = True
    elif lst[i + 1] - lst[i] <= -2:
      print('No')
      exit()
print('Yes')