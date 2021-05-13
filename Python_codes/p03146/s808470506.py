import math
def main():
  s = int(input())
  numarray=[s]
  ans=0
  i=1
  while True:
    if s%2==1:
      s=3*s+1
    else:
      s=int(s/2)
    if s in numarray:
      break
    else:
      numarray.append(s)
      i+=1
  print(i+1)
main()