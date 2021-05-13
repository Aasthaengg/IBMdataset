import math
def main():
  x = int(input())
  sum=0
  if x==0 or x==1:
    sum=x
  else:
    for i in range(2,int(math.sqrt(x))+1):
      j=2
      while True:
        if pow(i,j) <= x:
          if pow(i,j) > sum:
            sum=pow(i,j)
        else:
          break
        j+=1
  print(sum)
main()
