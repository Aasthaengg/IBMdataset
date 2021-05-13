h = -1
w = -1

while True:
  input = map(int, raw_input().split(" "))
  h = input[0]
  w = input[1]
  if (h == 0 and w == 0):
    break

  odd_line = ""
  even_line = ""

  j = 0
  while j < w:
    if j % 2 == 0:
      odd_line += "."
      even_line += "#"
    else:
      odd_line += "#"
      even_line += "."
    j += 1

  i = 0
  while i < h:
    if i % 2 == 0:
      print even_line
    else:
      print odd_line
    i += 1

  print ""