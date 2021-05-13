l = input()
arr = l.split(' ')
arr = [int(e) for e in arr]

if 1 <= arr[0] <= 100 and 1 <= arr[1] <= 100 and 1 <= arr[2] <= 100:
  if arr[0] == arr[1] + arr[2]:
    print('Yes')
  elif arr[1] == arr[2] + arr[0]:
    print('Yes')
  elif arr[2] == arr[0] + arr[1]:
    print('Yes')
  else:
    print('No')