S = input()

year,month,day = map(int,S.split("/"))

if year<2019:
  print("Heisei")
elif year==2019:
  if month<=4:
    print("Heisei")
  else:
    print("TBD")
else:
  print("TBD")