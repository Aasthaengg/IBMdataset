n = input()
num = [int(x) for x in n]

if sum(num) == 7:
  print(str(num[0])+"+"+str(num[1])+"+"+str(num[2])+"+"+str(num[3])+"=7")
elif num[0] -num[1] + num[2] + num[3] == 7:
  print(str(num[0])+"-"+str(num[1])+"+"+str(num[2])+"+"+str(num[3])+"=7")
elif num[0] -num[1] - num[2] + num[3] == 7:
  print(str(num[0])+"-"+str(num[1])+"-"+str(num[2])+"+"+str(num[3])+"=7")
elif num[0] -num[1] - num[2] - num[3] == 7:
  print(str(num[0])+"-"+str(num[1])+"-"+str(num[2])+"-"+str(num[3])+"=7")
elif num[0] +num[1] - num[2] - num[3] == 7:
  print(str(num[0])+"+"+str(num[1])+"-"+str(num[2])+"-"+str(num[3])+"=7")
elif num[0] +num[1] + num[2] - num[3] == 7:
  print(str(num[0])+"+"+str(num[1])+"+"+str(num[2])+"-"+str(num[3])+"=7")
elif num[0] - num[1] + num[2] - num[3] == 7:
  print(str(num[0])+"-"+str(num[1])+"+"+str(num[2])+"-"+str(num[3])+"=7")
elif num[0] +num[1] - num[2] + num[3] == 7:
  print(str(num[0])+"+"+str(num[1])+"-"+str(num[2])+"+"+str(num[3])+"=7")



