import math
def main():
  n=int(input())
  a=int(n/100)
  if a*100+a*10+a>=n:
    print(a*100+a*10+a)
  else:
    print((a+1)*100+(a+1)*10+a+1)
main()