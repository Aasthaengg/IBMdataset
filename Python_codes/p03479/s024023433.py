def func(x, y, count):
  new_x = x * 2
  if new_x > y:
    return count
  else:
    new_count = count + 1
    return func(new_x, y, new_count)
    
x, y = [int(i) for i in input().split()]

print(func(x, y, 1))