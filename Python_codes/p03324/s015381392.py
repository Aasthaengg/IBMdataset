import math
def main():
  d,n = list(map(int,input().split()))
  if n==100:
    n+=1
  print(pow(100,d)*n)
main()
