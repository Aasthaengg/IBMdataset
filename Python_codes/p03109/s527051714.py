y, m, d=map(int, input().split("/"))
if 2020<y:
  print("TBD")
else:
  if y<2019:
    print("Heisei")
    
  else:                   #y==2019
    if 5<=m:
      print("TBD")
    else:
      if m<=4:
        print("Heisei")