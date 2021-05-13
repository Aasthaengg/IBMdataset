def getGrade(m, f, r):
  grade = ""
  if m == -1 or f == -1:
    grade = "F"
  elif m + f >= 80:
    grade = "A"
  elif m + f >= 65:
    grade = "B"
  elif m + f >= 50:
    grade = "C"
  elif m + f >= 30:
    if r >= 50:
      grade = "C"
    else:
      grade = "D"
  else:
    grade = "F"
  return grade

while True:
  line = raw_input().split(" ")
  m = int(line[0])
  f = int(line[1])
  r = int(line[2])
  if m == -1 and f == -1 and r == -1:
    break
  else:
    print getGrade(m, f, r)