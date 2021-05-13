input_str = input()

while(True):
  if input_str[0:11] == "dreameraser":
    input_str = input_str[11:]
  elif input_str[0:10] == "dreamerase":
    input_str = input_str[10:]
  elif input_str[0:7] == "dreamer":
    input_str = input_str[7:]
  elif input_str[0:6] == "eraser":
    input_str = input_str[6:]
  elif input_str[0:5] == "dream" or input_str[0:5] == "erase":
    input_str = input_str[5:]
  else:
    print("NO")
    break
  
  if len(input_str) == 0:
    print("YES")
    break