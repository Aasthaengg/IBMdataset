import math
def main():
  s = input()
  t = input()
  flg=0
  for i in range(0,len(s)):
    s=s[len(s)-1:]+s[:len(s)-1]
    if s==t:
      flg=1
      break
  if flg==1:
    print("Yes")
  else:
    print("No")
main()
