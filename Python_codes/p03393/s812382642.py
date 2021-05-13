string = input()
if len(string) < 26:
  for i in range(97, 124):
    if chr(i) not in string:
      break
  print(string + chr(i))
else:
  val = [string[-1]]
  for i in string[-2::-1]:
    if i > val[-1]:
      val.append(i)
    else:
      break
  if len(val) == 26:
    print(-1)
  else:
    print(string[:-len(val)-1] + min(i for i in val if i > string[-len(val)-1]))
