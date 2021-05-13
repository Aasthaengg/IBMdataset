a = list(input())
b = list(input())
c = list(input())

win = False # if win == True, someone will win
run = a

while win != True:
  if run[0] == "a":
    run.pop(0)
    run = a # reset run
    if len(a) == 0:
      print("A")
      win = True
  elif run[0] == "b":
    run.pop(0)
    run = b
    if len(b) == 0:
      print("B")
      win = True
  else:
    run.pop(0)
    run = c
    if len(c) == 0:
      print("C")
      win = True



