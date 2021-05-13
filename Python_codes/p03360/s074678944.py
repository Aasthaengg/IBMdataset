import math
def main():
  a,b,c = list(map(int,input().split()))
  k = int(input())
  if a<b:
    if b<c:
      print(a+b+c*pow(2,k))
    else:
      print(a+b*pow(2,k)+c)
  else:
    if a<c:
      print(a+b+c*pow(2,k))
    else:
      print(a*pow(2,k)+b+c)
main()
