line = map(int, raw_input().split(" "))
count = 0
for value in range(line[0], line[1] + 1):
  if line[2] % value == 0:
    count += 1
print count