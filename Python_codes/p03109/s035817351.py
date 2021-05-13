Y,M,D=map(int,input().split("/"))
if((Y<=2019 and M <= 4 and D <= 30) or Y<= 2018):
  print("Heisei")
else:
  print("TBD")