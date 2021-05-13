a = [input() for i in range(2)]
s = a[0]
t = a[1]
my_result = 0
for i in range(3):
  if s[i] == t[i]:
    my_result += 1
  else:
    my_result += 0
print(my_result)