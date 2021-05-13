topping = list(map(str, input()))
count = 0
for i in range(len(topping)):
  if topping[i]=='o':
    count += 1
print(700 + 100*count)