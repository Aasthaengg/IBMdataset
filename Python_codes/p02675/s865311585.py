n = input()
word = n[-1]
 
if word == "3":
  print("bon")
elif word == "0" or word == "1" or word == "6" or word == "8":
  print("pon")
else:
  print("hon")