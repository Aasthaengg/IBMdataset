str_n = str(input())

temp = int(str_n[0])
temp = 111*temp

int_n = int(str_n)

if int_n > temp:
  temp = int(str_n[0])
  temp = temp+1
  print(111*temp)
else:
  temp = int(str_n[0])
  print(111*temp)