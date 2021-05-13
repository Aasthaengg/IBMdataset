N = int(input())
arr = sorted(list(map(int, input().split())))
divider = arr[0]
all = False
while not all:
  all = True
  new_arr = []
  for i in range(len(arr)):
    if arr[i] % divider > 0:
      all = False
      new_arr.append(arr[i] % divider)
  new_arr.append(divider)
  arr = sorted(new_arr)
  divider = new_arr[0]

print(divider)