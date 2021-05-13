s = input()
my_result = 700
for i in range(3):
  if s[i] == 'o':
    my_result += 100
  else:
    my_result += 0
print(my_result)