n = input()

x = len(n)-1


if n[x] == "2" or n[x] == "4" or n[x] == "5" or n[x] == "7" or n[x] == "9":
  print("hon")
  
elif n[x] == "0" or n[x] =="1" or n[x] == "6" or n[x] == "8":
  print("pon")
else:
  print("bon")