a = input()
arr = list(a)
if arr[-1] == "s":
  arr.insert(len(arr), "es")
  print("".join(arr))
else:
  arr.insert(len(arr), "s")
  print("".join(arr))