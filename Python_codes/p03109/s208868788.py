def main():
  s = input()
  if int(s[0:4])<=2018:
    print( "Heisei" )
  elif int(s[0:4])==2019:
    if int(s[5:7])<=4:
      print( "Heisei" )
    else:
      print( "TBD" )
  else:
      print( "TBD" )
  
main()