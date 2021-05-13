input = raw_input().split(" ")
list = []
for value in input:
  list.append(int(value))

length = len(list)
i = 0
while i < length - 1:
  min = list[i]
  j = i + 1
  while j < length:
    if list[i] > list[j]:
      temp = list[i]
      list[i] = list[j]
      list[j] = temp
    j += 1
  i += 1

print " ".join(map(str, list))