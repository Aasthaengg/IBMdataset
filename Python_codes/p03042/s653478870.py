s = input()

if ((int(s[0])==0 and 1<=int(s[1])<=9)  or (int(s[0]) == 1 and 0<=int(s[1])<=2)) and ((int(s[2])==0 and 1<=int(s[3])<=9)  or (int(s[2]) == 1 and 0<=int(s[3])<=2) ):
  print("AMBIGUOUS")
elif (int(s[0])==0 and 1 <=int(s[1])<=9)  or (int(s[0]) == 1 and 0<=int(s[1])<=2):
  print("MMYY")
elif (int(s[2])==0 and 1 <=int(s[3])<=9)  or (int(s[2]) == 1 and 0<=int(s[3])<=2):
  print("YYMM")
else:
  print("NA")
