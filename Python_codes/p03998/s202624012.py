import sys
sa = list(input())
sb = list(input())
sc = list(input())

def turn(s,n):
  if len(s)==0:
    print(n)
    sys.exit()
  tmp = s.pop(0)
  if tmp == "a":
    turn(sa,"A")
  elif tmp == "b":
    turn(sb,"B")
  elif tmp == "c":
    turn(sc,"C")
    
turn(sa,"A")