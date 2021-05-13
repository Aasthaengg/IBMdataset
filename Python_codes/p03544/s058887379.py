import math
def main():
  n = int(input())
  num=[0]*87
  num[0]=2
  num[1]=1
  for i in range(2,n+1):
    num[i]=num[i-1]+num[i-2]
  print(num[n])
    
main()
