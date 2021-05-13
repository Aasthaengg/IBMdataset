def solve(s):
  suma = 0
  for x in s:
    suma += int(x)
  if suma % 9 == 0:
    return True
  return False

s = input()
x = solve(s)
if x == True: print("Yes")
else: print("No")