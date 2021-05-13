n = int(raw_input())

residence = []

for i in xrange(4):
  floor = []
  for j in xrange(3):
    room = []
    for k in xrange(10):
      room.append(0)
    floor.append(room)
  residence.append(floor)

i = 0
while i < n:
  line = map(int, raw_input().split(" "))
  residence[line[0] - 1][line[1] - 1][line[2] - 1] += line[3]
  # print "residence[%d][%d][%d] = %d" % (line[0] - 1, line[1] - 1, line[2] - 1, line[3])
  # print residence
  i += 1

secion_line = "####################"
for i in xrange(4):
  for j in xrange(3):
    output_line = ""
    for k in xrange(10):
      output_line += " " + str(residence[i][j][k])
    print output_line
  if i != 3:
   print secion_line