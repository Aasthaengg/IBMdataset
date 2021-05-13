h = -1
w = -1

while True:
  input = map(int, raw_input().split(" "))
  h = input[0]
  w = input[1]
  if (h == 0 and w == 0):
    break

  i = 1
  j = 0
  inner_line = "#"
  outer_line = ""

  while j < w:
    outer_line += "#"
    if (j != 0 and j != w - 1):
      inner_line += "."
    j += 1
  inner_line += "#"

  print outer_line  
  while i < h - 1:
    print inner_line
    i += 1
  print outer_line

  print ""