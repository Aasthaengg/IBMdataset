input_list = input().split(" ")
syoumi = int(input_list[0])
mae = int(input_list[1])
eat = int(input_list[2])
if eat <= mae:
  print("delicious")
elif (eat - mae) <= syoumi:
  print("safe")
else:
  print("dangerous")