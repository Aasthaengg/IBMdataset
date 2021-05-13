def main():
  s = input()
  flg=0
  for i in range(0,len(s)):
    if (i+1)%2==1:
      print(s[i],end="")
  print()
main()