arr = [1,2,3]
one = int(input())
two = int(input())

arr[one-1] = 0
arr[two-1] = 0

for i in arr:
  if i > 0: print(i)