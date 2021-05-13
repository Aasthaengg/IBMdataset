s = input()
def serch(s):
  position_C = s.find("C")
  if position_C == -1:
    return False
  else:
    position_F = s.rfind("F")
    if position_F == -1:
      return False
    elif position_C < position_F:
      return True
    else:
      return False

if serch(s) == True:
  print("Yes")
else:
  print("No")