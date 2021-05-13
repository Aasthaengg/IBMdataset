s = input()
plus_len = len(s) - 1
num_search = 2 ** plus_len
result = 0
for i in range(num_search):
  x = ''
  for index,value in enumerate(s):
    x += value
    if (i >> index) & 1:
      x += '+'
  
  #print(x)
  #print(eval(x))
  result += eval(x)
print(result)