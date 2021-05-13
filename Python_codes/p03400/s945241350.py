import math
def main():
  n = int(input())
  d,x = list(map(int,input().split()))
  for i in range(0,n):
    a = int(input())
    x+=(int((d-1)/a)+1)
  print(x)
  
main()
