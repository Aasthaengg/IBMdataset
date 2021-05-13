def main():
  s=input()
  x = s.find("C")
  y = s.find("F")
  if x<0 or y<0:
    print("No")
    return 0
  while x<len(s):
    if s[x]=="F":
      print("Yes")
      return 0
    x+=1
  print("No")
  

    
main()
