num_array = list(map(int, input().split()))
if num_array[0] <= num_array[2] and num_array[2] <= num_array[1]:
  print("Yes")
else:
  print("No")