
input_line = input().split()

distance = int(input_line[0])
remain = int(input_line[1])
speed = int(input_line[2])

time = distance/speed

if time > remain:
  print("No")
else:
  print("Yes")
