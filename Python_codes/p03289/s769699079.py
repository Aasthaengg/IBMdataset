import math
def main():
  s = input()
  flg=0
  if s[0]=='A':
    if s[2:len(s)-1].count('C')==1:
      s=s.replace('C','c')
      if s[1:].islower():
        print("AC")
        flg=1
  if flg==0:
    print("WA")
main()
