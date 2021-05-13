S = input()

def is_good(code):
  if code[0] == code[1] or code[1] == code[2] or code[2] == code[3]:
    return False
  return True

if is_good(S):
  print('Good')
else:
  print('Bad')