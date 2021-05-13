arr = []
for _ in range(4):
  arr.append(int(input()))

if arr[1] > arr[0]:
  arr[1] = arr[0]
charge = arr[1]*arr[2] + (arr[0]-arr[1])*arr[3]
print(charge)