from math import ceil
lst = []
ten = []
for i in range(5):
  t = int(input())
  if t % 10 == 0:
    ten.append(t)
  else:
    lst.append(t)
if lst == []:
  print(sum(ten))
  exit()
x = min(lst, key=lambda x: x % 10)
lst.remove(x)
for i in range(len(lst)):
  lst[i] = 10 * (lst[i] // 10 + 1)
print(x + sum(lst) + sum(ten))