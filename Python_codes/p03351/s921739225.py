arr = []
A, B, C, D = map(int, input().split())

arr.append(A)
arr.append(B)
arr.append(C)
arr = sorted(arr)

if abs(C-A) <= D:
  print("Yes")
elif arr[1]-arr[0] <= D and arr[2]-arr[1] <= D:
  print("Yes")
else:
  print("No")