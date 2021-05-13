A=input()
B=input()
C=input()
ListA=list(A)
ListB=list(B)
ListC=list(C)
pile = "a"
res = ""
for i in range(400):
  if pile == "a":
    pile = ListA.pop(0)
  elif pile == "b":
    pile = ListB.pop(0)
  else:
    pile = ListC.pop(0)
  if len(ListA) == 0 and pile == "a":
    res = "A"
    break
  elif len(ListB) == 0 and pile == "b":
    res = "B"
    break
  elif len(ListC) == 0 and pile == "c":
    res = "C"
    break
  else:
    pass
print(res)