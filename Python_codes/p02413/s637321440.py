input_list = raw_input().split(" ")
r = int(input_list[0])
c = int(input_list[1])

i = 0
array = []
while i < r:
  input_line = raw_input().split(" ")
  array.append(map(int, input_line))
  i += 1

# print array

for i in xrange(len(array)):
  sum = 0
  for j in xrange(len(array[i])):
    sum += array[i][j]
  array[i].append(sum)

# print array

list = []
for i in xrange(c + 1):
  sum = 0
  for j in xrange(r):
    sum += array[j][i]
  list.append(sum)
array.append(list)

for i in xrange(r + 1):
  output = ""
  for j in xrange(c + 1):
    output += " " + str(array[i][j])
  print output.strip()