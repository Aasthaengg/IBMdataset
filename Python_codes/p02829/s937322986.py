A = int(input())
B = int(input())

ls = [1,2,3]
for num in ls:
  if num == A or num == B:
    continue
  print(num)