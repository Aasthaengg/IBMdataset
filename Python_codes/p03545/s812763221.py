s = [int(x) for x in list(input())]

def joinstring(s, op1, op2, op3):
  return str(s[0]) + op1 + str(s[1]) + op2 + str(s[2]) + op3 + str(s[3]) + "=7"

p = "+"
m = "-"

if s[0] + s[1] + s[2] + s[3] == 7:
  print(joinstring(s, p, p, p))
elif s[0] + s[1] + s[2] - s[3] == 7:
  print(joinstring(s, p, p, m))
elif s[0] + s[1] - s[2] + s[3] == 7:
  print(joinstring(s, p, m, p))
elif s[0] - s[1] + s[2] + s[3] == 7:
  print(joinstring(s, m, p, p))
elif s[0] + s[1] - s[2] - s[3] == 7:
  print(joinstring(s, p, m, m))
elif s[0] - s[1] + s[2] - s[3] == 7:
  print(joinstring(s, m, p, m))
elif s[0] - s[1] - s[2] + s[3] == 7:
  print(joinstring(s, m, m, p))
elif s[0] - s[1] - s[2] - s[3] == 7:
  print(joinstring(s, m, m, m,))
