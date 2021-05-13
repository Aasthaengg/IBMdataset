hitatistr = input()
count = 0
flag = "ok"
for i in hitatistr:
  if count % 2 == 0:
    if i != "h":
      flag = "ng"
      break
  else:
    if i != "i":
      flag = "ng"
  count = count + 1
if flag == "ok" and count >= 2 and count % 2 == 0:
  print("Yes")
else:
  print("No")

