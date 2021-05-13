array = input().split()
for _ in array:
  if array.count(_) == 1:
    print(_)
    break