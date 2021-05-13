pc = ""
for c in list(input()):
  if pc == c:
    print('Bad')
    exit()
  else:
    pc = c
print('Good')