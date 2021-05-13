input = raw_input().split(" ")
input = map(int, input)

w = input[0]
h = input[1]
x = input[2]
y = input[3]
r = input[4]

if w < (x + r) or (x - r) < 0 or (y + r) > h or (y - r) < 0:
  print "No"
else:
  print "Yes"