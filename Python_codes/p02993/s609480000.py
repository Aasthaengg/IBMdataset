nb = [int(x) for x in input()]
def solo(nb):
  for loop in range(3):
    if nb[loop] == nb[loop+1]:
      return ("Bad")
  return "Good"
print(solo(nb))
