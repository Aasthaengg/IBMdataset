S=input()
month=int(S[5:7])
day=int(S[8:10])
if (month==4 and day<=30) or month<4 :
  print("Heisei")
else :
  print("TBD")