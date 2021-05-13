string = input().strip()
hi_string = "hi" * (len(string)//2)
if string == hi_string:
  print("Yes")
else:
  print("No")