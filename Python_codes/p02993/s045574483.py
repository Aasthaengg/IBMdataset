arr = list(input())
for k in range(len(arr) - 1):
  if arr[k] == arr[k+1]:
    print("Bad")
    exit()
print("Good")
