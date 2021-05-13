s=input()
if int(s[:4])<2019:
  print("Heisei")
elif int(s[:4])>2019:
  print("TBD")
else:
  if s[5]=="0":
    if int(s[6])<5:
      print("Heisei")
    else:
      print("TBD")
  else:
    print("TBD")