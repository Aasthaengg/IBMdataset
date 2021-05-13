str = str(input())
list = list(str)
a = len(list)
if a == 2:
  print(str)
else:
  list.reverse()
  ans = ' '
  for i in list:
    ans += i
  print(ans)